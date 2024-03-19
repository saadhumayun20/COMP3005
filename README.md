Author: Saad Humayun, 101259608

The StudentsTable.sql file provides the schema to create the table as well as to insert the inital values into the table.
The python script already has this included, the .sql file was provided just incase.

install command for setting up python3 script (run inside terminal):  python3 -m pip install psycopg2-binary

You can uncomment the function calls at the bottom and modify them with your own parameters to test

Make sure pgadmin is running and you are connected to your server, and check if the db_params in the python script match that of your database.

To run the python script (run in directory with the python file): python3 assignment3_part_1_COMP3005.py

Run this query in pgadmin using the query tool to check the table: SELECT * FROM students

**Ensure that the function calls at the bottom are uncommented or you won't see changes**

Link to demo video: https://youtu.be/af6DhawTPZw
