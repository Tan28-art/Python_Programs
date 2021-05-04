s = input("Enter a string here: ")
count = 0

for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
    elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        count += 1

print("No. of vowels = ", count)