#to check if the no. is an armstrong number
'''n=int(input("Enter No. here:"))

t = n

s = 0

for i in range(n):
    r = n % 10
    s = s + r**3
    n = n // 10

if t==s:
    print("Your number is an armstrong number")
else:
    print("Your number is not an armstrong number")'''

        # or

n = int(input("enter number here: "))

s = 0

for i in str(n):
    s = s + int(i)**3

if s == n:
    print("Armstrong no.")
else:
    print("Not")

