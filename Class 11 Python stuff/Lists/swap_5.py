l = eval(input("List: "))
c = 0

for i in l:
    c += 1

i = 0

while i<c-1:
    if l[i] % 5 ==0:
        l[i],l[i+1]=l[i+1],l[i]
        i+=1    
    i+=1
print(l)