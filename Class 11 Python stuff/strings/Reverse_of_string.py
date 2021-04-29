string = input("Enter a string here(In either upper or lower case): ")

new_s = ''

'''l = 0

for i in string:
    l+=1 

for j in range(l-1,-1, -1):  # from -1 to 0 in steps of -1
    new_s += string[j]

print(new_s)'''

    #or

for i in string:
    new_s = i + new_s

print(new_s)
#if new_s == string:
    #print("The given string is a palindrome")
#else:
    #print("It is not a palindrome")
