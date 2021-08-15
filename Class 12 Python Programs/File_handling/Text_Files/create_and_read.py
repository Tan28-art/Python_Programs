# # To create file and read 
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'a')
n = int(input("No. of lines: "))

for i in range(n):
    s = input("Enter line: ")
    f.write(s+'\n')

f.close()

f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')
print(f.read())
f.close()

