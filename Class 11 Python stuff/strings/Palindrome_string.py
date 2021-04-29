# Checking if the string is a palindrome or not
s = input("Enter string here: ")
s1 = ''

for i in s:
    s1 = i + s1

if s == s1:
    print("Palindrome")
else:
    print("Not a palindrome")