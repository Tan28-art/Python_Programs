p=input("Enter a character here:")
if p >= 'A' and p <= 'Z':
    print("It is a upper case character")
elif p >= 'a' and p <= 'z':
    print("It is a lower case character")
elif p >= '0' and p <= '9':
    print("It is a number")
else:
    print("It is a special character")
