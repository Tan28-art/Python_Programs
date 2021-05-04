d = {}
ch = "y"

while ch == "y":
    key = int(input("Key: "))
    val = input("Value: ")
    d[key] = val
    ch = input("Do you wish to continue?(y/n): ")

print()
print(d)
