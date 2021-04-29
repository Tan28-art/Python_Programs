s = input("Enter a string here: ")
ch = input("Enter character to find here: ")
count = 0

for i in s:
    count += 1

for i in range(count):
    if ch == s[i]:
        print("Index of", ch, "is", i)
        break
else:
    print("Character not found")

'''s = input("Enter a string here: ")
ch = input("Enter character to find here: ")

coun = -1

for i in s:
    coun += 1
    if ch == i:
        print("Index of", ch, "is", coun)
        break
else:
    print("Character not found")'''