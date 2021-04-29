l = eval(input("Enter list here: "))
el = float(input("Enter element to count here: "))
c = -1

for i in l:
    c += 1
    if i == el:
        print("index of", el, "=", c)
        break
else:
    print("element not found")    
