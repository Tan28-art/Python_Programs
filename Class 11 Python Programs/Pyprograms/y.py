# x^0-x^1+x^2-x^3...x^n
x = int(input("Enter no. here:"))
n = int(input("Enter power here:"))
s = 0
for i in range(n + 1):
    if i % 2 == 0:
        s += x ** i
    else:
        s -= x ** i
print(s)
a = int(input("Enter 1st no:"))
b = int(input("Enter 2nd no.:"))
s3 = 0
s4 = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        s3 += i
    else:
        s4 += i
print(s3)
print(s4)
