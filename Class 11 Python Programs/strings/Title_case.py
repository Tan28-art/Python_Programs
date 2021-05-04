s = input("String: ")
s1 = ''
c = 0

for i in s:
    c += 1

if 'a' <= s[0] <= 'z':
    s1 += chr(ord(s[0])-32)
else:
    s1 += s[0]

i = 1

while i < c:

    if s[i] == '':
        s1 += s[i]

        if 'a' <= s[i+1] <= 'z':
            s1 += chr(ord(s[i+1])-32)
        else:
            s1 += s[i+1]
        i += 1
    
    else:
        s1 += s[i]
    
    i += 1

print(s1)



"""s = input("string: ")
s1 = ""
n = 0

for i in s:
    n += 1

if s[0] >= "a" and s[0] <= "z":
    s1 += chr(ord(s[0]) - 32)
else:
    s1 += s[0]
i = 1
while i < n:
    if s[i] == " ":
        s1 += s[i]
        if s[i + 1] >= "a" and s[i + 1] <= "z":
            s1 += chr(ord(s[i + 1]) - 32)
        else:
            s1 += s[i + 1]
        i = i + 1
    else:
        s1 += s[i]
    i += 1
print(s1)"""