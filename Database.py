import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='1234')
if conn.is_connected():
    print('Connection established')
#print(conn)

mycursor=conn.cursor()
mycursor.execute('Create Database pythondb')
print('mycursor')    