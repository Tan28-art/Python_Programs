import mysql.connector

con = mysql.connector.connect(user='root', password='your_password', host='localhost', database='your_db')
cur = con.cursor()

e = int(input("Enter Emp No. whose record has to be deleted: "))

cur.execute(f"delete from emp where eno = {e};")

con.commit()

cur.execute("select * from emp;")

data = cur.fetchall()

for i in data:
    print(i[0],i[1],i[2],i[3],i[4])
