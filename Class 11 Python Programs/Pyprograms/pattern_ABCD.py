#if input is ABCD then output is
'''
A
BB
CCC
DDDD
'''

s = input("Enter string: ")
c = 0

for i in s:
    c+=1

for i in range(c):
    print(s[i]*(i+1))