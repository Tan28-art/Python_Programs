# sum of number ending wiht 7 or 9
l = eval(input("Enter list here: "))
sum = 0

for i in l:
    if i%10 == 7 or i%10 == 9:
        sum += i

print("Sum is: ", sum)