import mysql.connector
db = mysql.connector.connect( host = "localhost",
user= "root",
password= "agsadf")
if db:
    print("connection is successful")
else:
    print("connection is unsuccessful")
