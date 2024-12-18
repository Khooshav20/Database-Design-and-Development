# Database-Design-and-Development
Garage Management Database System
@author Bundhoo Khooshav Nikhil


Database Description:

Consider a database that manages vehicle repairs in a garage. The database should capture all
the information mentioned in this scenario.

A garage handles multiple vehicles, each of which may require several repairs. The database
will store detailed information about each vehicle, including its vin, make, model, and year.
Every vehicle will also have exactly one owner, and the database will track the owner's details
namely identity number, name, phone and email. An owner can have multiple vehicles.
Not all vehicles that enter the garage may require repairs, but the database should still track
them regardless. The system must store the vehicle's information even if it is only there for
routine maintenance.

Every repair is associated with a specific vehicle. A vehicle can undergo multiple repairs, but
each repair is unique to that vehicle. That is, there will not be two identical repairs for the same
vehicle. The date of the repair should also be kept.

Repairs involve a combination of mechanics and parts. Each repair may require one or more
mechanics, depending on its complexity. Mechanics have their own information namely their
identity number, name, phone, address and specialisation. The database should keep track of
which mechanics work on which repairs to ensure efficient resource management.
A repair may involve the use of multiple parts. Each part has a part number, name and price.
Parts can be used in different repairs. Each step in a repair may require different mechanics and
parts.

The database will provide robust support for various use cases, including generating a list of
vehicles repaired during the current month along with their associated costs, and allowing
searches for vehicle owners by name. Additionally, the system will enable browsing of owners
and their vehicles for easy reference. To address the relationship between repairs and
mechanics, an intermediary table will associate repairs with 


---------------------------------------------------------------------------------------------------------

Welcome to the Garage Database Proposal project! This system efficiently manages vehicle repairs in a garage, tracking vehicles, their owners, repairs, mechanics, and parts used.


- Files Included

garage.db: The SQLite database file containing all the necessary data.

garage.py: A Python script that provides a command-line interface to interact with the database.


- Getting Started

Ensure both garage.db and garage.py are located in the same folder.

Run the script by executing the following command in your terminal:

python garage.py or python3 garage.py 

Once the script runs, you will be presented with a command-line interface offering 5 options to interact with the garage database.


- Demo

For a detailed walkthrough of the database and its functionality, check out the demo video here:

https://youtu.be/daD_HNZ8dso 


Enjoy using the Garage Database System!
