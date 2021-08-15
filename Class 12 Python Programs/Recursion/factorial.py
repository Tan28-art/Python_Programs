def fact(a):
    if a == 1:  # Base Condition
        return 1
    else:   # Recursive condition
        return a * fact(a-1)    

x = int(input("Enter number whose factorial is to be found: "))
print(fact(x))