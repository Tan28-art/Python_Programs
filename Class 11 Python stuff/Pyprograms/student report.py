rno = int(input("Enter roll number:"))
name = input("Enter name here:")
m1 = float(input("Enter math marks here:"))
m2 = float(input("Enter english marks here:"))
m3 = float(input("Enter computer marks here:"))
m4 = float(input("Enter physics marks here:"))
m5 = float(input("Enter chemistry marks here:"))
tm = m1 + m2 + m3 + m4 + m5
per = tm / 5
if 91 <= per <= 100:
    grade = "A1"
elif 80 <= per <= 90:
    grade = "A2"
elif 70 <= per < 80:
    grade = "B1"
elif 60 <= per < 70:
    grade = "B2"
elif 50 <= per < 60:
    grade = "C1"
elif 40 <= per < 50:
    grade = "D"
else:
    grade = "fail"
print("Name:", name)
print("Roll No.:", rno)
print("Total marks scored:", tm)
print("Percentage:", per)
print("Grade:", grade)

