s = input("Enter a string in UPPER case: ")
s1 = ''
#A=65 a=97 diff is 32

for i in s:
    x = ord(i) + 32
    y = chr(x)
    s1 = s1 + y

print("Lower case =", s1)