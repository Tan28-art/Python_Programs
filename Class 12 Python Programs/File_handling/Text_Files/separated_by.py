# To read a file and separate all words with #
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')

l = f.read().split()

print('#'.join(l))

f.close()