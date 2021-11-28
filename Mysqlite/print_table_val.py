import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="fgdfgfd3",
    database="t20wc"
    )
m=db.cursor()
m.execute("select *from batsmen")
pd=m.fetchall()#to fetch all data from database
for i in pd:
    print(i)
