s = input("Enter a string here: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for j in s:
    if j == "a" or j == "A":
        a += 1

    elif j == "e" or j == "E":
        e += 1

    elif j == "i" or j == "I":
        i += 1

    elif j == "o" or j == "O":
        o += 1

    elif j == "u" or j == "U":
        u += 1

print("No. of a = ", a)
print("No. of e = ", e)
print("No. of i = ", i)
print("No. of o = ", o)
print("No. of u = ", u)
