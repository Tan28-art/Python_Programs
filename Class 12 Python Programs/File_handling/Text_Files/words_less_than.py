# to display words less than 4 chars

f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')

l = f.read().split()

for i in l:
    if len(i) < 4:
        print(i)

f.close()