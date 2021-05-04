a=int(input("Enter 1st no:"))
b=int(input("Enter 2nd no.:"))
s1=0
s2=0
while a<=b: 
    if a%2==0:
        s1+=a
    else:
        s2+=a
    a+=1
print("Sum of even numbers is :",s1)
print("Sum of odd numbers is :",s2)

    