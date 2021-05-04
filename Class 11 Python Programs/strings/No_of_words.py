s = input("Ener a string here: ")

count = 1

for i in s:
    if i == " ":
        count += 1

print("No. of words present are", count)