# Read a txt file and replace every occurance of h with q

f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')
s = f.read()
s1 = s.replace('h', 'q')
f.close()
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'w')
f.write(s1)
f.close()
