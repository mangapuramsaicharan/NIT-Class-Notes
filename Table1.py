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

# SQL query with corrected placeholders
sql = 'INSERT INTO student (name, branch, id) VALUES (%s, %s, %s)'
val = [
    ('john', 'CSE', 5),
    ('mike', 'IT', 7),
    ('Tyson', 'ME', 9)
]

# Execute the query
mycursor.executemany(sql, val)
conn.commit()

# Print the number of inserted rows
print(mycursor.rowcount, 'records inserted')