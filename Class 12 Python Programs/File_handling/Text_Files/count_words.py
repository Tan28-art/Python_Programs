f = open(r'C:\Tanish\Python\Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')


#word_count = 0
# for i in f:
#     l = i.split()
#     word_count += len(l)
    
        #or

s = f.read()
l = s.split()
print("No. of words: ", len(l))
