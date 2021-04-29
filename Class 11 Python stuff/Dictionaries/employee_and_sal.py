d = {}
ch = "y"

while ch == "y":
    name = input("Name: ")
    salary = float(input("Salary: "))
    d[name] = salary
    ch = input("Do you wish to continue?(y/n): ")

print()
print(d)
print()

for i in d:
    print(i, d[i])
