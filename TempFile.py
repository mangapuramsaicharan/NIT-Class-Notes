from EMPREGISTRATION import get_db_connection


def load_students():
    # Remove all previous entries in the Treeview
    for row in load_students.get_children():
        load_students.delete(row)

    try:
        # Establish a connection to the database
        conn = get_db_connection()  # Assumes get_db_connection() is defined elsewhere
        cursor = conn.cursor()

        # Execute the query to fetch all data from the registration table
        cursor.execute("SELECT * FROM registration")
        rows = cursor.fetchall()

        # Insert each row into the Treeview
        for row in rows:
            load_students.insert("", "end", values=row)

    except Exception as e:
        print(f"Error loading students: {e}")

    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()
