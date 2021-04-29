'''l = eval(input("List: "))

x = l[0]
y = l[0]

for i in l:
    if x>i:
        x=i

print("Min = ", x)

# max

for i in l:
    if y<i:
        y=i

print("Max = ", y)
 '''























l = eval(input("Enter list: "))

ma, mi = l[0], l[0]

for i in l:
    if ma<i:
        ma = i
    
    if mi>i:
        mi = i

print(f"Min of list is {mi} and Max of list is {ma}")

