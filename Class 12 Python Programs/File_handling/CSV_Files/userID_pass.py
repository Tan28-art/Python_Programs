# Create a csv file by entering userid and password (both str)
# Search for a given userid and show the password
import csv

def create_csv():
    f = open(r'Class 12 Python Programs\File_handling\CSV_Files\user.csv', 'w', newline='')
    w = csv.writer(f, delimiter=',')
    ch = 'y'
    while ch == 'y':
        l = []
        user = input('Enter User ID: ')
        user_pass = input('Enter Password: ')
        l += [user, user_pass]
        w.writerow(l)
        ch = input("Continue?(y/n): ")
    f.close()
    return

def search_pass():
    f = open(r"Class 12 Python Programs\File_handling\CSV_Files\user.csv", "r")
    user = input('Enter userID to search: ')
    r = csv.reader(f)
    for i in r:
        if i[0] == user:
            print(i[1])

    f.close()