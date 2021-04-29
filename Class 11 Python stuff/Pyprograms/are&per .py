import math

print("Menu")
print("1:square")
print("2:rectangle")
print("3:circle")
print("4:triangle")

x = int(input("Enter your choice here:"))

if x == 1:
    s = float(input("Enter length of side of square:"))
    a = s * s
    p = 4 * s
    print("area:", a)
    print("perimeter", p)

elif x == 2:
    rs1 = float(input("Enter length of rectangle here:"))
    rs2 = float(input("Enter breadth of rectangle here:"))
    print("Area:", rs1 * rs2)
    print("Perimeter:", 2 * (rs1 + rs2))

elif x == 3:
    r = float(input("Enter the radius of the circle:"))
    circumference = 2 * math.pi * r
    ar = math.pi * (r ** 2)
    print("Circumference of the circle is:", circumference)
    print("Area of the circle is:", ar)

elif x == 4:
    a = float(input("Enter 1st side of triangle:"))
    b = float(input("Enter 2nd side of triangle:"))
    c = float(input("Enter 3rd side of triangle:"))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    peri = a + b + c
    print("Area:", area)
    print("Perimeter:", peri)
