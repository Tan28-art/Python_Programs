# Function to count occurance of he and she
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')

def He_She_Count():
    l = f.read().split()
    print("He: ", l.count('he'))
    print("She: ", l.count('she'))
    f.close()

He_She_Count()
f.close()            

