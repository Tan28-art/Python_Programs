# x^0-x^1+x^2-x^3...x^n
x = int(input("Enter no. here:"))
n = int(input("Enter power here:"))
s = 0
i = 0
while i <= n:
    if i % 2 == 0:
        s += x ** i
    else:
        s -= x ** i
    i += 1

print(s)
print("Result is :", s)

