# create emp.dat
# Emp no, ename and sal
# create a menu based progam for
# i) displaying the data (ii) search for particular employee and display it
# iii) Update the salary of a particular employee (iv) increase all sal by 500
# v) delete the details of given emp

import pickle


def Write_Binary():
    f = open(f"Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat", "wb")

    choice = "y"
    while choice.lower() == "y":
        l = []
        try:
            emp_no = int(input("Enter Employee No.: "))
            ename = input("Enter Employee name: ")
            sal = float(input("Enter Salary: "))
        except ValueError:
            print("Please enter a valid value.")
        l += [emp_no, ename, sal]
        pickle.dump(l, f)
        choice = input("Do you wish to continue?(y/n):  ")
    f.close()


def Read_file():
    f = open(f"Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat", "rb")
    try:
        while True:
            l = pickle.load(f)
            print(l)
    except EOFError:
        pass

    f.close()


def Retrieve():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat", "rb")
    emp_no = int(input("Enter Emp number to retrieve: "))
    flag = 0  # Flag variable
    try:
        while True:
            l = pickle.load(f)
            if l[0] == emp_no:
                print("Name: ", l[1])
                print("Salary: ", l[2])
                print()
                flag = 1

    except EOFError:
        pass

    if flag == 0:
        print("Emp number not found.")
    f.close()


def update_sal():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat", "rb+")
    rn = int(input("Enter emp no to update: "))
    m = float(input("Enter salary to update: "))
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

    f.close()


def delete_rec():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat", "rb")
    g = open("Class 12 Python Programs\\File_handling\\Binary_Files\\temp.dat", "wb")

    import os

    rn = int(input("Enter emp no to delete: "))
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
    os.remove("Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat")
    os.rename(
        "Class 12 Python Programs\\File_handling\\Binary_Files\\temp.dat",
        "Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat",
    )


def sal_add_500():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\emp.dat", "rb+")

    try:
        while True:
            position = f.tell()
            l = pickle.load(f)
            l[2] += 500    
            f.seek(position)
            pickle.dump(l, f)

    except EOFError:
        pass

    f.close()


def menu():
    print() # Empty line
    print("Choose an option.")
    print("1) Display Employee Data")
    print("2) Search Employee")
    print("3) Update salary")
    print("4) Increase all salary by 500")
    print("5) Delete particular Employee Details")
    print("6) Exit\n")
    

# Write_Binary()  # Initializes the employee file with data


# Main program loop
while True:
    menu()
    try:
        x = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if x not in [1, 2, 3, 4, 5, 6]:
        print("Please Enter a valid option.")
    elif x == 1:
        Read_file()
    elif x == 2:
        Retrieve()
    elif x == 3:
        update_sal()
    elif x == 4:
        sal_add_500()
    elif x == 5:
        delete_rec()
    elif x == 6:
        break

