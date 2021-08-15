# Ceate employee.csv
# Emp no, Ename, Salary, Dept No.
# Count and display the total no of organizations

import csv

def create_csv():
    f = open(r'Class 12 Python Programs\File_handling\CSV_Files\employee.csv', 'w', newline='')
    w = csv.writer(f, delimiter=',')
    ch = 'y'
    while ch == 'y':
        l = []
        eno = int(input("Employee No:"))
        ename = input("Employee Name: ")
        sal = int(input("Salary: "))
        dept = int(input("Dept No.: "))
        l += [eno, ename, sal, dept]
        w.writerow(l)
        ch = input("Continue?(y/n): ")
    f.close()
    return

def count_emp():
    f = open(r'Class 12 Python Programs\File_handling\CSV_Files\employee.csv', 'r')
    count = 0
    r = csv.reader(f)
    for i in r:
        count+=1
    f.close()
    return count

def avg_sal():  # Find avg salary of a partocu;ar departement
    f = open(r'Class 12 Python Programs\File_handling\CSV_Files\employee.csv', 'r')
    dept = int(input("Enter department no.: "))
    total = 0
    count = 0
    r = csv.reader(f)

    for i in r:
        if dept == int(i[3]):
            total += int(i[2])
            count += 1

    f.close()
    avg = total/count
    print("Average salary: ", avg)

create_csv()

avg_sal()