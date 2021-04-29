n = int(input("Enter No. here:"))
s = 0
for i in str(n):
    r = n % 10
    n = n // 10
    s = s + r
    print(r, end="")
print("\nSum is", s)

