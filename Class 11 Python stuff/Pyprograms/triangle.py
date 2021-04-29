a=float(input("Enter 1st side of triangle here"))
b=float(input("Enter 2nd side of triangle here"))
c=float(input("Enter 3rd side of triangle here"))
if a+b>c and b+c>a and a+c>b:
    print("The sides form a triangle")
else:
    print("These sides do not form a triangle")