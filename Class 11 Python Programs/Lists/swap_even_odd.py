#To swap the elements at even locations with those at odd positions
l = eval(input("Enter list here: "))

s=0

for i in l:
    s+=1

for i in range(0, s-1, 2):
    l[i], l[i+1] = l[i+1], l[i]

print("List: ", l)