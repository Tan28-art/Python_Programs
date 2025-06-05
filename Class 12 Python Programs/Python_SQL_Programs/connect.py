import mysql.connector

con = mysql.connector.connect(user='root', password='your_password', host='localhost', database='your_db')

cur = con.cursor()
cur.execute('select * from emp;')

data = cur.fetchall()

print("eno   ename\t  salary   phone no  dept")

for i in data:
    print(i)
