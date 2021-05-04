'''# To swap first half of the list with the second half
l = eval(input("List: "))
c = 0

for i in l:
    c += 1

ml = c // 2  # Middle term of list

if c % 2 == 0:
    m = ml
else:
    m = ml + 1

print(ml, m)

for i in range(0, ml):
    l[i], l[m] = l[m], l[i]
    m += 1

print(l)
'''

l = eval(input("Enter list: "))
c = 0

for i in l:
    c+=1

mid = c//2 if c%2 == 0 else c//2+1

for i in range(mid):
    if (i+mid) < c:
        l[i], l[mid+i] = l[mid+i], l[i]

print(l)
