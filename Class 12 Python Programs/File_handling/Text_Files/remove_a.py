# Program to remove lines starting with a and put it in another file

def remove_add():
    f = open(r'Class 12 Python Programs\File_handling\Text_Files\test_text.txt', 'r')
    g = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'w')
    l = f.readlines()
    i = 0
    
    while i < len(l):
        if l[i].lower().startswith("a"):
            g.write(l[i])
            l.remove(l[i])
        else:
            i += 1

    g.close()
    f.close()
    f = open(r"Class 12 python Programs\File_handling\test_text.txt", "w")
    f.writelines(l)
    f.close()


remove_add()
