s = input("Enter a string in lower case: ")
s1 = ''
#A=65 a=97 diff is 32
for i in s:

    if 97<=ord(i)<=122:
        x = ord(i) - 32
        y = chr(x)
        s1 = s1 + y
    else:
        s1 = s1 + i

print("Upper case =", s1)
