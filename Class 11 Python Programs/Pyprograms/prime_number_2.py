x = int(input("Enter number: "))

if x>1:
    for i in range(2, x//2+1):
        if x%i == 0:
            print(x, "is composite")
            break
    else:
        print(x,"is prime")

elif x == 0 or x == 1:
    print("Neither prime nor composite")
