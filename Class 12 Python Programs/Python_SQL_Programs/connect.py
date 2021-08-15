import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='Tan*357498',  database='tan_db')

cur = con.cursor()
cur.execute('select * from emp;')

data = cur.fetchall()

print("eno   ename\t  salary   phone no  dept")

for i in data:
    print(i)
