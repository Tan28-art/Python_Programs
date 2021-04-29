# to count occurance of a character in a string

s = input("Enter a string here: ")
ch = input("Enter character here: ")

count = 0
for i in s:
    if ch == i:
        count +=1

print(ch, "occurs", count, "times in", s)
