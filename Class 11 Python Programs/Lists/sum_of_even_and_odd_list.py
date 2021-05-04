l = eval(input("List: "))

even = 0
odd = 0

for i in l:
    if i%2==0:
        even += i
    else:
        odd += i

print("Odd sum: ", odd)
print("Even sum: ", even)