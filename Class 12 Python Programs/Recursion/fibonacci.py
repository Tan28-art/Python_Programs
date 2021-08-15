# Fibonacci using recursion
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

n = int(input("Enter the number of terms: "))

for i in range(1,n+1):
    print(fib(i))
