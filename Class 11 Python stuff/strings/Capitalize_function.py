# capitalize the first letter and convert rest of the string to lowercase

s = input("Enter string here: ")
s1 = ""

l = 0

for x in s:
    l += 1

if 'a' <= s[0] <= 'z':
    s1 = s1 + chr(ord(s[0]) - 32)
else:
    s1 += s[0]

for i in range(1, l, 1):
    if 'A'<=s[i]<='Z':
        s1 += chr(ord(s[i]) + 32)
    else:
        s1 += s[i]

print(s1)

    # or

'''for i in s[1:]:
    if i == " ":
        s1 += i
    if "A" <= s[i + 1] <= "Z":
        s1 += chr(ord(s[i + 1]) - 32)
    else:
        s1 += s[i + 1]
'''


