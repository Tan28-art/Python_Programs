#0, 1, 1, 2, 3, 5, 8, 13 .....
x=int(input("terms in series:"))
f=0
s=1

print(f)
print(s)

for i in range(1,x,1):
    i=f+s
    print(i)
    f=s
    s=i



