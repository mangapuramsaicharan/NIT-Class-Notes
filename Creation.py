import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='pythondb'
)

# Create a cursor object
mycursor = conn.cursor()

# SQL query to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY,name VARCHAR(100),branch VARCHAR(50)
)
"""


# Execute the query
mycursor.execute(create_table_query)

# Confirm table creation
print("Table 'student' created successfully.")

# Close the connection
mycursor.close()
conn.close()
