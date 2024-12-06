import sqlite3

DB_PATH = "garage.db"

def connect_db(db_path):
    """Connect to the SQLite3 database."""
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def get_current_month_repair_vehicles(conn):
    """Retrieve vehicles repaired during the current month."""
    query = """
      SELECT v.vin, v.make, v.model, r.date, r.cost
      FROM Vehicle v
      JOIN Repair r ON v.vin = r.vin
      WHERE strftime('%m', r.date) = strftime('%m', 'now')
      AND strftime('%Y', r.date) = strftime('%Y', 'now')
    """
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\nVehicles Repaired During the Current Month:")
        print("-" * 100)
        for vehicle in results:
            print(f"VIN: {vehicle[0]} \tMake: {vehicle[1]} \tModel: {vehicle[2]} \tRepair Date: {vehicle[3]} \tCost: {vehicle[4]}")
    else:
        print("No vehicles repaired during the current month")

def search_owner_by_name(conn, search):
    """Retrieve owner by name."""
    query = "SELECT * FROM Owner WHERE name LIKE ?"
    cursor = conn.cursor()
    cursor.execute(query, (f"%{search}%",))
    results = cursor.fetchall()
    if results:
        print("\nOwners Found:")
        print("-" * 120)
        for owner in results:
            print(f"Identity Number: {owner[0]} \tName: {owner[1]} \tPhone: {owner[2]} \tEmail: {owner[3]}")
    else:
        print(f"No owners found with name {search}")

def list_repairs_and_mechanics(conn):
    """Retrieve repairs and the mechanics who handled them."""
    query = """
        SELECT r.repair_id, r.date, r.cost, m.name
        FROM Repair r
        JOIN RepairMechanic rm ON r.repair_id = rm.repair_id
        JOIN Mechanic m ON rm.mechanic_id_num = m.identity_number
    """
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("\nRepairs and Mechanics:")
        print("-" * 80)
        for repair in results:
            print(f"Repair ID: {repair[0]} \tDate: {repair[1]} \tCost: {repair[2]} \tMechanic: {repair[3]}")
    else:
        print("No repairs found")

def browse_owners_and_vehicles(conn):
    """Browse owners and their vehicles."""
    cursor = conn.cursor()
    
    # List all owners
    cursor.execute("SELECT * FROM Owner")
    owners = cursor.fetchall()
    
    if not owners:
        print("No owners found.")
        return
    
    print("\nOwners:")
    print("-" * 125)
    for owner in owners:
        print(f"Identity Number: {owner[0]} \tName: {owner[1]} \tPhone: {owner[2]} \tEmail: {owner[3]}")
    
    # Let the user choose an owner
    owner_id = input("\nEnter the identity number of the owner to view their vehicles: ")
    
    # List vehicles for the chosen owner
    query = """
        SELECT v.vin, v.make, v.model, v.year
        FROM Vehicle v
        WHERE v.owner_id_num = ?
    """
    cursor.execute(query, (owner_id,))
    vehicles = cursor.fetchall()
    
    if vehicles:
        print(f"\nVehicles for Owner ID {owner_id}:")
        print("-" * 80)
        for vehicle in vehicles:
            print(f"VIN: {vehicle[0]} \tMake: {vehicle[1]} \tModel: {vehicle[2]} \tYear: {vehicle[3]}")
    else:
        print(f"No vehicles found for Owner ID {owner_id}")

def main():
    print("-" * 34)
    print("Welcome to the Garage Database App")
    print("-" * 34)
    conn = connect_db(DB_PATH)

    if not conn:
        print("Failed to connect to the database. Exiting...")
        return

    while True:
        print("\n" + "-" * 10)
        print("Main Menu:")
        print("-" * 10)
        menu = [
            "List of vehicles repaired during the current month and their cost",
            "Search for vehicle owners by name",
            "List repairs and the mechanics who handled them",
            "Browse owners and their vehicles",
            "Exit"
        ]

        for i, item in enumerate(menu, 1):
            print(f"{i}. {item}")

        choice = input(f"\nEnter your choice ({1}-{len(menu)}): ")

        match choice:
            case "1":
                get_current_month_repair_vehicles(conn)
            case "2":
                search = input("Enter search name: ")
                search_owner_by_name(conn, search)
            case "3":
                list_repairs_and_mechanics(conn)
            case "4":
                browse_owners_and_vehicles(conn)
            case "5":
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select an option from the menu.")

    conn.close()

if __name__ == "__main__":
    main()
