#To count the occurance of a and e in a txt file
f = open(r'C:\Tanish\Python\Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')

count_a = 0
count_e = 0

for i in f:
    count_a += i.lower().count('a')
    count_e += i.lower().count('e')

f.close()
print(count_a)
print(count_e)