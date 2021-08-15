# Count lines that start with A
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')

def count_A():
    count = 0
    for i in f:
        if i.lower().startswith('a'):
            count += 1
    return count

f.close()
