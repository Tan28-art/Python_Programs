# To recursively compute greatest common divisor 
def gcd(a,b):
    r = b % a
    if r == 0:
        return a
    else:
        return gcd(r,a)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(gcd(a,b))