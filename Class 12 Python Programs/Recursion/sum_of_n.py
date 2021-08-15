# To recursively compute the sum of n natural numbers

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

x = int(input("Enter n: "))
print(sum(x))