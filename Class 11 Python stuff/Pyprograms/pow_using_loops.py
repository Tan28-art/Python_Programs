a = float(input("Enter base here:"))
b = int(input("Enter exponent here:"))
if b < 0:
    b = -b  # to make b positive
    a = 1 / a
p = 1

for i in range(b):
    p = p*a

print(a, "to the power", b, "is:", p)

