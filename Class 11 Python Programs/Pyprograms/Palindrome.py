# Checking if the number is a palindrome

n = int(input("Enter No. here:"))
reversed_no = 0
t = n

for i in str(n):
    r = n % 10
    reversed_no = reversed_no * 10 + r
    n = n // 10

# checking if the no is a palindrome

if t == reversed_no:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
