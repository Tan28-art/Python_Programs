#To count no. of letters, numbers and special characters
s = input("Enter your string here: ")

alpha = 0
digit = 0
special = 0

for i in s:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        alpha += 1
    elif ord('0')<=ord(i)<=ord('9'):
        digit += 1
    else:
        special += 1

print('alphabets =', alpha)
print("digits =", digit)
print("special =", special)