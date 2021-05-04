l = eval(input("List: "))

s = 0

for i in l:
    s += i*i

print(s)

'''l = eval(input("List: "))

n = 0

for i in l:
    n += 1

for i in range(0, n//2):
    l[i],l[n-i-1] = l[n-i-1],l[i]

print(l)'''