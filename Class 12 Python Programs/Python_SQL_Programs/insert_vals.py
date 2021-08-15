import mysql.connector

con = mysql.connector.connect(user='root', password='Tan*357498', host='localhost', database='tan_db')
cur = con.cursor()

n = int(input("Enter te no of records to insert: "))

for i in range(n):
    eno = int(input("Enter Emp No.: "))
    ename = input("Enter Emp name: ")
    salary = int(input("Enter salary: "))
    phone = int(input("Enter Emp phone number: "))
    dept = int(input("Enter Dept No.: "))

    cur.execute(f"insert into emp values ({eno}, '{ename}', {salary}, {phone}, {dept});")
# we need o save these changes permanently thus we need to use .commit()
con.commit()

cur.execute("select * from emp;")

data = cur.fetchall()

for i in data:
    print(i[0],i[1],i[2],i[3],i[4])
