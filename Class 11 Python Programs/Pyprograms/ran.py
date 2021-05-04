p = int(input("Enter principal amount here:"))
r = float(input("Enter interest rate here:"))
t = int(input("Enter duration here:"))
ci = p * (1 + (r / 100)) ** t
amt = p - ci
print("The compound interest is:", ci)
print("The amount is:", amt)
