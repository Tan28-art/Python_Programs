d = {}
ch = "y"
c = 0

while ch == "y":
    key = int(input("Key: "))
    val = input("Value: ")
    d[key] = val
    ch = input("Do you wish to continue?(y/n): ")
    c += 1

print()
print(d)
print("Length of dict: ", c)
