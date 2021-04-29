s = input("Enter a string in lower case: ")
s1 = ''
#A=65 a=97 diff is 32
for i in s:
    x = ord(i) - 32
    y = chr(x)
    s1 = s1 + y

print("Upper case =", s1)
