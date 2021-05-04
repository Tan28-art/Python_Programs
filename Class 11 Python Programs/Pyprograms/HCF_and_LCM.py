#To find HCF and LCM of 2 numbers
x = int(input("Enter no. here:"))
y = int(input("Enter no. here:"))

if x < y:
    p, q = x, y
else:
    p, q = y, x

while p > 0:
    r = q % p
    if r == 0:
        h = p
        print("HCF is:", h)
    q, p = p, r
    
lcm = (x * y) // h
print("LCM is:", lcm)

