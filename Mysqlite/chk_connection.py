import mysql.connector
db = mysql.connector.connect( host = "localhost",
user= "root",
password= "Simba@123")
if db:
    print("connection is successful")
else:
    print("connection is unsuccessful")
