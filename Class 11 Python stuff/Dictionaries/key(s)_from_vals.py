d = {}
ch = "y"

while ch == "y":
    name = input("Name: ")
    salary = float(input("Salary: "))
    d[name] = salary
    ch = input("Do you wish to continue?(y/n): ")
    print()

print()

# When salary is given

f = 0 # flag variable

y = float(input("Enter salary: "))
for i in d:
    if d[i] == y:
        print("Employees with Salary", y, "=", i)
        f = 1        
if f == 0:
    print("Employee with salary", y, "not found")     
       