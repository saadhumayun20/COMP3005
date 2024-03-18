#Saad Humayun, 101259608

import psycopg2

# Make sure pgAdmin and you are connected to the server so this runs as intended

# Database connection parameters
# These can be changed according to your own database
db_params = {
    'dbname': 'Assignment3Part1',
    'user': 'postgres',
    'password': '1234567890',
    'host': 'localhost'
}

# Function to connect to the database
def db_connect(func):
    """Decorator to handle database connection and cursor for any function."""
    def with_connection_(*args, **kwargs):
        conn = psycopg2.connect(**db_params)
        try:
            retval = func(conn, *args, **kwargs)
        except Exception as e:
            conn.rollback()
            print(f"Database operation failed: {e}")
            return None
        else:
            conn.commit()
        finally:
            conn.close()
        return retval
    return with_connection_

# Checks if table in database is already made, otherwise it creates and populates it with default values
@db_connect
def resetAndCreateTable(conn):
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS students;")
    cur.execute("""
        CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        );
    """)
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    """)

# This function gets all the students from the table and displays them
@db_connect
def getAllStudents(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    for record in cur.fetchall():
        print(record)

# This function adds a new student to the table
@db_connect
def addStudent(conn, first_name, last_name, email, enrollment_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))

# This function updates an existing students email
@db_connect
def updateStudentEmail(conn, student_id, new_email):
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id))

# This function deletes all elements of a specific student from the table
@db_connect
def deleteStudent(conn, student_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))

if __name__ == "__main__":
    resetAndCreateTable()                                                      # Call the create table

    print("Fetching initial list of students...") 
    getAllStudents()                                                           # Calls the getAllStudents function to show the original table
    
    # Below are the rest of the functions commented out so we don't call them each time we run our program
    # If you want to run any function uncomment the functions (along with the print statements for clarity)
    # After uncommenting you may modify the function call to your liking

    #print("\nAdding a new student...")
    #addStudent('Lebron', 'James', 'lebron@example.com', '2024-01-01')      # Adds a new student to the table
    #print("\nFetching updated list of students after adding a new one...")
    #getAllStudents()                                                           # Gets all students to show new student
    
    #print("\nUpdating Lebrons's email...")
    #updateStudentEmail(4, 'lebron.new@example.com')                            # Update existing students students email using student_id
    #print("\nFetching updated list of students after updating email...")       
    #getAllStudents()                                                           # Gets all students to show updated email
    
    #print("\nDeleting Lebron from students...")
    #deleteStudent(4)                                                          # Deletes exisiting student using their student_id
    #print("\nFetching final list of students after deletion...")
    #getAllStudents()                                                           # Gets all students to show updated email
