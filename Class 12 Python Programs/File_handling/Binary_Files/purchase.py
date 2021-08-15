# Create a bin file purchase.dat
# Purchase ID, Desc, Qty
# Accept the details of one item and add it to the end of the file


import pickle


def Create_Purchase():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\purchase.dat", "wb")

    choice = "y"
    while choice.lower() == "y":
        l = []
        pur_id = int(input("Enter Purchase ID: "))
        desc = input("Enter Description: ")
        qty = int(input("Enter quantity: "))
        l += [pur_id, desc, qty]
        pickle.dump(l, f)
        choice = input("Do you wish to continue?(y/n):  ")
    f.close()


def Read_Purchase():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\purchase.dat", "rb")
    try:
        while True:
            l = pickle.load(f)
            print(l)
    except EOFError:
        print("Success")

    f.close()


def Add_Item():
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\purchase.dat", "ab")
    l = []
    pur_id = int(input("Enter Purchase ID: "))
    desc = input("Enter Description: ")
    qty = int(input("Enter quantity: "))
    l += [pur_id, desc, qty]
    pickle.dump(l, f)
    f.close()


def Show_Purchase(id):
    f = open("Class 12 Python Programs\\File_handling\\Binary_Files\\purchase.dat", "rb")
    try:
        
        while True:
            l = pickle.load(f)
            if l[0] == id:
                print("Desc", l[1])
                print("Qty", l[2])
            
    except EOFError:
        print("Success")

    f.close()
# Create_Purchase()
Read_Purchase()
# Add_Item()
# Read_Purchase()
id = int(input("Enter Purchase ID: "))
Show_Purchase(id)
