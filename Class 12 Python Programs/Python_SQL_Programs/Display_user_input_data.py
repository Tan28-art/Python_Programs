import mysql.connector

con = mysql.connector.connect(user='root', password='your_password', host='localhost', database='your_db')

cur = con.cursor()
e = int(input("Enter Emp no: "))
cur.execute(f'select * from emp where eno = {e};')

data = cur.fetchall()
row_count = cur.rowcount

for i in data:
    print(i[0], i[1], i[2], i[3], i[4])

print("Rows fetched: ", row_count)
