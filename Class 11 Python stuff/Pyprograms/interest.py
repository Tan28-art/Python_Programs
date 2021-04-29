# program to calculate simple interest
p = float(input("Enter principle amount here:"))
r = float(input("Enter Interest rate here(in %):"))
t = float(input("Enter Time here(in Years):"))
si = p * r * t / 100
am = p + si
print("The simple interest is:", si)
print("The Amount is:", am)
