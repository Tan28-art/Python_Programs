eno = int(input("Enter employee number:"))
ename = input("Enter Name here:")
bsal = float(input("Enter basic salary here:"))
hra = (10 / 100) * bsal
da = (5 / 100) * bsal
ta = (2 / 100) * bsal
gs = bsal + hra + da + ta
tax = (5 / 100) * gs
nsal = gs - tax
if nsal > 50000:
    grade = "A"
if 25000 <= nsal <= 50000:
    grade = "B"
if nsal < 25000:
    grade = "C"
print("Employee Number:", eno)
print("Employee Name:", ename)
print("Basic salary:", bsal)
print("Hra:", hra)
print("Da:", da)
print("Ta:", ta)
print("Tax:", tax)
print("Gross Salary:", gs)
print("Net Salary:", nsal)
print("Grade:", grade)

