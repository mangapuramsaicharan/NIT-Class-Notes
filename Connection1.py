import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='pythondb')

mycursor=conn.cursor()
mycursor.execute('show tables')

for x in mycursor:
    print(x)
    