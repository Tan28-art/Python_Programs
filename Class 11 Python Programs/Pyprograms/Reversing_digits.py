'''n = int(input("Enter No. here:"))
for i in n:
    r = n % 10
    n = n // 10
    print(r, end="")'''

        #OR

'''n = int(input("Enter No. here:")) 
while n>0:
    r = n%10
    n=n//10
    print(r ,end='')'''

n = int(input("Enter no: "))
n1 = ''
for i in str(n):
    n1 = i + n1

print(n1)