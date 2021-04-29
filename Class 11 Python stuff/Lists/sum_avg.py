l = eval(input("Enter list here: "))
s = 0
c = 0

for i in l:
    c += 1
    s += i

avg = s/c

print("Sum of elements: ", s)
print("Average: ", avg)