Author: Saad Humayun, 101259608

install command:  python3 -m pip install psycopg2-binary

You can uncomment the function calls at the bottom and modify them with your own parameters to test

Make sure pgadmin is running and you are connected to your server, and check if the db_params in the python script match that of your database.

To run the python script: python3 assignment3_part_1_COMP3005.py

Run this query in pgadmin using the query tool to check the table: SELECT * FROM students

Schema for creating the table (written inside the python script along with the inital values):

  CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        );

Link to demo video: https://youtu.be/xIcMf35gJJw
