# To find the Employee with highest Salary in a dictionary and display it
d = {}
ch = "y"

while ch == "y":
    Employee = input("Employee: ")
    Salary = float(input("Salary: "))
    d[Employee] = Salary
    ch = input("Do you wish to continue?(y/n): ")
    print()

print(d)

a = Employee

for i in d:
    if d[i] > d[a]:
        a = i

print("Employee with highest Salary is", a, "with a salary of:", d[a])
