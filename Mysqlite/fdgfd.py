import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Simba@123",
    database="t20wc"
)
m=db.cursor()
m.execute("CREATE TABLE Nm_usr(serial INT AUTO_INCREMENT Primary key, Reg_No varchar(200),Password varchar(200))")