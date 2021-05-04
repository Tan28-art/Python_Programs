# Checking if a number is a prime number

n = int(input("Enter a number here: "))

# flag variable

f = 0

if n == 0 or n == 1:
    print(n, "is neither prime nor composite")

else:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            f = 1
            break
    if f == 0:
        print("Your number is a prime number")
    else:
        print("Your number is not a prime number")
