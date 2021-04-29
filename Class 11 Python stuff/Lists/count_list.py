l = eval(input("Enter list here: "))
el = float(input("Enter element to count here: "))
c = 0

for i in l:
    if i == el:
        c += 1
        
print(el, "appears", c, "times in", l)