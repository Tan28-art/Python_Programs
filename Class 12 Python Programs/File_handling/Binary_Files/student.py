# Creating and reading from a binary file
import pickle

def Write_Binary(file):
    f = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\{file}.dat', 'wb')
    
    choice = 'y'
    while choice.lower() == 'y':
        l = []
        roll = int(input('Enter Roll No.: '))
        name = input('Enter name: ')
        mark = float(input('Enter marks: '))
        l += [roll, name, mark]
        pickle.dump(l, f)
        choice = input("Do you wish to continue?(y/n):  ")
    f.close()

def Read_file(file):
    f = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\{file}.dat', 'rb')
    try:
        while True:
            l = pickle.load(f)
            print(l)
    except EOFError:
        pass

    f.close()

# Retrieve data based on roll number 
def Retrieve(file):
    f = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\{file}.dat', 'rb')
    rn = int(input("Enter roll number to retrieve: "))
    flag = 0 # Flag variable
    try:
        while True:
            l = pickle.load(f)
            if l[0] == rn:
                print("Name: ", l[1])
                print("Marks: ", l[2])
                flag = 1
        
    except EOFError:
        pass

    if flag == 0:
            print("Roll number not found.")
    f.close()
# Display student with marks above 90
def above_ninety(file):
    f = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\{file}.dat', 'rb')

    try:
        while True:
            l = pickle.load(f)
            if l[2] > 90:
                print("Name: ", l[1])
            
    except EOFError:
        pass

# To update marks of a particular student
def update_mark(file):
    f = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\{file}.dat', 'rb+')
    rn = int(input("Enter roll no to update: "))
    m = float(input("Enter marks to update: "))
    try:
        while True:
            position = f.tell()
            l = pickle.load(f)
            if l[0] == rn:
                l[2] = m
                f.seek(position)
                pickle.dump(l, f)

    except EOFError:
        pass

# To delete a record
def delete_rec(file):
    f = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\{file}.dat', 'rb')
    g = open(f'Class 12 Python Programs\\File_handling\\Binary_Files\\temp.dat', 'wb')

    import os
    rn = int(input("Enter roll no to delete: "))
    try:
        while True:
            l = pickle.load(f)
            if rn != l[0]:
                pickle.dump(l, g)
            else:
                continue

    except EOFError:
        pass
    f.close()
    g.close()
    os.remove("Class 12 Python Programs\\File_handling\\Binary_Files\\student.dat") 
    os.rename('Class 12 Python Programs\\File_handling\\Binary_Files\\temp.dat', 'Class 12 Python Programs\\File_handling\\Binary_Files\\student.dat')

file = input("Enter file name: ")    
# Retrieve(file)
# above_ninety(file)
# update_mark(file)
delete_rec(file)
Read_file(file)




'''
import pickle
def above_ninety(file):
    f = open('FACTORY.DAT', 'rb')
    print("FCTID\tFCTNAME\tPROD")
    try:
        while True:
            l = pickle.load(f)
            if l[0] 105:
                print(l[0], l[1], l[2])
            
    except EOFError:
        pass
'''