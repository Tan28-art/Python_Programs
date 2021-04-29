# To display elements and their locations which are not multiples of 2 or 3

l = eval(input("Enter list here: "))
index = -1

for i in l:
    index += 1
    if i%2 == 0 or i%3 == 0:
        continue
    else:
        print(i, "is not divisible by 2 or 3 and is present at: ", index)

