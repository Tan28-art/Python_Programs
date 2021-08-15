# # To create file and read using list
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'w')
n = int(input("No. of lines: "))
l = []

for i in range(n):
    s = input("Enter line: ")
    l += [s+'\n']

f.writelines(l)
f.close()

f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')
print(f.read())
f.close()

