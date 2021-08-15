f = open(r'C:\Tanish\Python\Class 12 Python Programs\File_handling\new.txt', 'r')

s = f.read()
l = s.split()
word = input("Enter word to count: ")
count = 0

for i in l:
    if i.lower() == word:
        count += 1

f.close()
print(count)