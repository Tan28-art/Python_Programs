# To count the occurrence of stuff using a dictionary
s = eval(input("List: "))
# l = s.split() # for words in string
d = {}

for i in s: # replace with l for string
    if i not in d:
        c = 0 # Counter variable
        for j in s: # replace with l for string
            if  i == j:
                c += 1
            d[i] = c

print(d)