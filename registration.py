import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='webgui'
)

# Create a cursor object
mycursor = conn.cursor()

# SQL query to insert data
sql = "INSERT INTO registration (id, name, course, fee) VALUES (%s, %s, %s, %s)"
val = (1, 'John Doe', 'Python', 500)

# Execute the query
mycursor.execute(sql, val)
conn.commit()

# Confirm insertion
print(mycursor.rowcount, "record inserted.")

# Close the connection
mycursor.close()
conn.close()
