import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Simba@123",
    database="t20wc"
    )
m=db.cursor()
s=input("enter the name")
val=(s,)
sql="select *from batsmen where Name=%s"
m.execute(sql,val)

pd=m.fetchone()#to fetch all data from database
print(pd)
for i in pd:
    print(i,' | ')#it will be having 1 tuple inside list
    # for p in i:
        # print(p,' ')
