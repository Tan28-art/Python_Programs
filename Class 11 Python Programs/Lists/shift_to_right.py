'''l = eval(input("List: "))
c = 0

for i in l:
    c += 1

x = l[c-1]

l.remove(x)
l.insert(0,x)

for i in range(c-1,0,-1):
    l[i] = l[i-1]
l[0] = x

print(l)'''


l = eval(input("Enter list: "))
c = 0

for i in l:
    c+=1

for i in range(1,c):
    l[0], l[i] = l[i], l[0]

print(l)