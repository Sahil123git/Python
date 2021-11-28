import mysql.connector#don't execute this is for creating new table
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Simba@123",
    database="t20wc"
)
d
m=db.cursor()
m.execute("CREATE TABLE Nam_usr(serial INT AUTO_INCREMENT Primary key, Reg_No varchar(200),Password varchar(200))")