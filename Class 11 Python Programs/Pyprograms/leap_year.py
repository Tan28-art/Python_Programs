p = int(input("Enter a year here:"))
if p % 4 == 0 and p % 100 != 0:
    print("It is a leap year")
elif p % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
