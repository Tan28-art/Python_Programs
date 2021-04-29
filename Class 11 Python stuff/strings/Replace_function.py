s = input("Enter a string here: ")
ch1 = input("Enter character to find: ")
ch2 = input("Enter character to replace here: ")

s1 = ''

for i in s:
    if ch1 == i:
        s1 += ch2
    else:
        s1 += i

if s == s1:
    print("Character not found")
else:
    print(s1)