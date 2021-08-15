# copy the sentecnes of one file to another if the line contains a
f = open(r'C:\Tanish\Python\Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')
g = open(r'C:\Tanish\Python\Class 12 Python Programs\File_handling\Text_Files\sec.txt', 'w')

for i in f:
    if 'a' in i.lower():
        g.write(i)

f.close()
g.close()