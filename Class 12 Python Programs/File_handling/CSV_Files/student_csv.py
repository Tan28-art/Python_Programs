import csv


def create_csv():
    f = open(r"Class 12 Python Programs\File_handling\CSV_Files\student.csv", "w", newline="")
    w = csv.writer(f, delimiter=",")
    ch = "y"
    while ch == "y":
        l = []
        rn = int(input("Roll No:"))
        name = input("Name: ")
        marks = int(input("Marks: "))
        l += [rn, name, marks]
        w.writerow(l)
        ch = input("Continue?(y/n): ")
    f.close()
    return\


def read_csv():
    f = open(r"Class 12 Python Programs\File_handling\CSV_Files\student.csv", "r")
    r = csv.reader(f)
    print("roll no\t name\t marks")
    for i in r:
        print(i[0], i[1], i[2])
    f.close()
    return


def search():
    f = open(r"Class 12 Python Programs\File_handling\CSV_Files\student.csv", "r")
    rn = int(input("Enter roll no. to be searched: "))
    r = csv.reader(f)
    for i in r:
        if int(i[0]) == rn:         # Data stored in the form of strings so we need to convert 
            print(i[1], i[2])

    f.close()


def above_ninety():
    f = open(r"Class 12 Python Programs\File_handling\CSV_Files\student.csv", "r")
    r = csv.reader(f)
    count = 0

    for i in r:
        if int(i[2]) > 90:
            print(i[0], i[1])
            count += 1

    f.close()
    print("No. of students with marks above ninety: ", count)


def start_with_a(): # Function to display students whose names start with a
    f = open(r"Class 12 Python Programs\File_handling\CSV_Files\student.csv", "r")
    r = csv.reader(f)
    for i in r:
        if i[1].lower().startswith("a"):
            print(i[0], i[1], i[2])

    f.close()

create_csv()
start_with_a()