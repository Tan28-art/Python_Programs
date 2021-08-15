f = open(r'Class 12 Python Programs\File_handling\new.txt', 'r')

for i in range(4):
    print(f.readline(), end = '')
    print(f.tell())