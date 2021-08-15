def compute(a, b):
    if b == 0:
        return 1
    else:
        return a * compute(a, b-1)

x = int(input("Enter base: "))
y = int(input("Enter exponent: "))

print(compute(x, y))
