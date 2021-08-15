#To count the number of lines in a txt file
f = open(r'C:\Tanish\Python\Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')
# s = f.readline()

# while s:
#     print(s, end = '')
#     s = f.readline()

        #or

count = 0

for i in f:
    print(i, end = '')
    count+=1

print()
print(count)
f.close()   