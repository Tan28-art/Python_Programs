# accepting length and breadth of a rectangle and printing its area and perimeter
Length = int(input("Enter the length of the rectangle"))
breadth = int(input("Enter the breadth of the rectangle"))
peri = 2 * (Length + breadth)
area = Length * breadth
print("Perimeter of rectangle:", peri)
print("Area of rectangle:", area)
