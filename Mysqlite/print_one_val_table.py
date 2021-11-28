import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Simba@123",
    database="t20wc"
    )
m=db.cursor()
sql="select * from batsmen where Name=%s"
us_val=input()# %s tojk set value runtime
val=(us_val,)

m.execute(sql,val)
pd=m.fetchone()
print(pd)
