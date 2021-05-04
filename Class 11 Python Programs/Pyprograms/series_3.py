# x+x^2/2!-x^3/3!
x = int(input("Enter base here:"))
n = int(input("Enter power here:"))
s = 0
f = 1
for i in range(1, n + 1, 1):
    f = f * i
    if i == 1:
        s += (x ** i) / f
    elif i % 2 == 0:
        s += (x ** i) / f
    else:
        s -= (x ** i) / f
print("Result of series is:", s)


    #or

'''x = int(input("Enter base here:"))
n = int(input("Enter power here:"))
s = x
for i in range(2,n+1,1):
    f = 1

    for j in (1,i+1,1):
        f = f*j

    if i % 2 == 0:
        s += (x ** i) / f

    else:
        s -= (x ** i) / f
print(s)'''
