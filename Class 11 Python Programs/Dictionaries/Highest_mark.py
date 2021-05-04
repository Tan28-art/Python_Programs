# To find the student with highest marks in a dictionary and display it
d = {}
ch = "y"

while ch == "y":
    Student = input("Student: ")
    Marks = float(input("Marks: "))
    d[Student] = Marks
    ch = input("Do you wish to continue?(y/n): ")
    print()

print(d)

a = Student

for i in d:
    if d[i] > d[a]:
        a = i

print("Student with highest marks is:", a, "with", d[a], "Marks")
