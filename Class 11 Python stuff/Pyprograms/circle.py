# Finding area and circumference of a circle
r = int(input("Enter the radius of the circle:"))
import math
circum = 2 * math.pi * r
ar = math.pi * (r ** 2)
print("Circumference of the circle is:", circum)
print("Area of the circle is:", ar)

