import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Simba@123",
    database = "t20wc"
    )
m = db.cursor()
sql="INSERT INTO batsmen(Team,Name, Matches, Runs) VALUES(%s,%s,%s,%s)"
val=[
    ("pk","ba",6,700),
    ("Nfdz","lk",6,354)]
m.executemany(sql,val)
db.commit()
