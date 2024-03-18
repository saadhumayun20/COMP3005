import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'Assignment3Part1',
    'user': 'postgres',
    'password': '1234567890',
    'host': 'localhost'
}

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

@db_connect
def resetAndCreateTable(conn):
    cur = conn.cursor()
    # Drop the existing table
    cur.execute("DROP TABLE IF EXISTS students;")
    # Create the table anew
    cur.execute("""
        CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        );
    """)
    # Insert initial data
    cur.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    """)

@db_connect
def getAllStudents(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    for record in cur.fetchall():
        print(record)

@db_connect
def addStudent(conn, first_name, last_name, email, enrollment_date):
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date))

@db_connect
def updateStudentEmail(conn, student_id, new_email):
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id))

@db_connect
def deleteStudent(conn, student_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))

if __name__ == "__main__":
    resetAndCreateTable()
    # Fetch and display all students initially.
    print("Fetching initial list of students...")
    getAllStudents()
    
    # Add a new student.
    print("\nAdding a new student...")
    addStudent('Alice', 'Wonderland', 'alice@example.com', '2024-01-01')
    
    # Fetch and display all students to see the newly added student.
    print("\nFetching updated list of students after adding a new one...")
    getAllStudents()
    
    # Update the email of the newly added student.
    print("\nUpdating Alice's email...")
    updateStudentEmail(4, 'alice.new@example.com')  # Assuming '4' is Alice's student_id. Adjust accordingly.
    
    # Fetch and display all students to see the updated email.
    print("\nFetching updated list of students after updating email...")
    getAllStudents()
    
    # Delete the newly added student.
    print("\nDeleting Alice from students...")
    deleteStudent(4)  # Assuming '4' is Alice's student_id. Adjust accordingly.
    
    # Fetch and display all students to confirm deletion.
    print("\nFetching final list of students after deletion...")
    getAllStudents()
