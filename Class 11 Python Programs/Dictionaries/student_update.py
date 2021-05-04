d = {}
ch = "y"

while ch == "y":
    Student = input("Student: ")
    Marks = float(input("Marks: "))
    d[Student] = Marks
    ch = input("Do you wish to continue?(y/n): ")
    print()
    
print(d)

print()

x = input("Enter student whose marks have to be updated: ")
y = float(input("Enter marks to update here: "))
for i in d:
    if i == x:
        d[i] = y
        break
else:
    print("Student not found.")

print(d)