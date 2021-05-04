d = {}
ch = "y"

while ch == "y":
    name = input("Name: ")
    salary = float(input("Salary: "))
    d[name] = salary
    ch = input("Do you wish to continue?(y/n): ")
    print()

print()

# When employee salary is to be found

x = input("Enter employee to find: ")
for i in d:
    if i == x:
        print("Salary of", x, "=", d[i])
        break
else:
    print("Employee not found.")

# When salary is given and employee with that salary is to be found

f = 0 # flag variable

y = float(input("Enter employee to find: "))
for i in d:
    if d[i] == y:
        print("Employees(s) with Salary ", y, "is/are", i)
        f = 1        
if f == 0:
    print("Employee with salary", y, "not found")     
       