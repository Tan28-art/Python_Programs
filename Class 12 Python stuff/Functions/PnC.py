n = int(input("Enter n: "))
r = int(input("Enter r: "))

def fact(no):
    f = 1
    for i in range(1, no+1):
        f = f * i

    return f

perm = fact(n)/fact(n-r)
comb = fact(n)/(fact(r)*fact(n-r))

print(perm, comb)