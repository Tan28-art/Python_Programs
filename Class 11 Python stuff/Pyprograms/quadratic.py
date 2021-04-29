import math

a = float(input("Enter coefficient of x^2:"))
b = float(input("Enter coefficient of x:"))
c = float(input("Enter constant:"))
d = b ** 2 - 4 * a * c

if d < 0:
    print("Roots are complex and imaginary")
elif d >= 0:
    x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    y = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("Roots are:", x, ",", y)

