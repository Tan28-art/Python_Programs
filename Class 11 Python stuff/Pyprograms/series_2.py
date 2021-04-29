# x+(x^2/2)-(x^3/3)+x^4/4...
x = int(input("Enter base here:"))
n = int(input("Enter power here:"))
s = 0
for i in range(1, n + 1, 1):
    if i == 1:
        s += (x ** i) / i
    elif i % 2 == 0:
        s += (x ** i) / i
    else:
        s -= (x ** i) / i
print("Result of series is:", s)

