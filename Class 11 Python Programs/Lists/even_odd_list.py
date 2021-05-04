#add 5 to odd nos in list and mutilpy by 10 the even nos
L = eval(input("List: "))
c = 0
for i in L:
    c+=1

for i in range(0,c):
    if L[i]%2==0:
        L[i]=L[i]*10
    else:
        L[i]=L[i]+5

print(L)
