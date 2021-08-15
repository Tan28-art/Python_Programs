from Bank_application import Bank_account
import sys

# List to store customer data
customers = []

print("Welcome to SimpleBank")
print()

# Menu
while True:

    print("1. Create a new account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. List all Accounts")
    print("5. Exit")

    print()

    ans = int(input("Enter your choice here (1-5): "))

    print()

    try:
        if ans not in [1, 2, 3, 4, 5]:  # Checks for invalid inputs
            raise RuntimeError  # This will raise runtimeerror which will be taken care of by except block, this prevents prigram from crashing

        elif ans == 1:
            id = input("Enter your id: ")
            name = input("Enter your name here: ")
            amount = int(input("Enter Amount: "))

            # creating the customer account

            cust_acc = Bank_account(
                id, name, amount
            )  # This will use the user info to create acc using the class from bank_application
            customers.append(
                cust_acc
            )  # This will add the acc to the list with all the accs (customers)

        elif ans == 2:
            deposit = 0
            identity = input("Enter your id here: ")

            for cust in customers:
                if (
                    cust.id == identity
                ):  # Checks if the user has an acc, if not else block is executed
                    deposit = int(input("Enter the amount to deposit :"))
                    cust.deposit_money(deposit)
                    cust.print_cust()

        elif ans == 3:
            withdraw = 0
            identity = input("Enter your id here: ")

            for cust in customers:
                if cust.id == identity:
                    withdraw = int(input("Enter the amount to withdraw :"))
                    cust.withdraw_money(withdraw)
                    cust.print_cust()

        elif ans == 4:
            password = input("Enter the password to access this data: ")

            if password == "1029384": 
                for cust in customers:
                    cust.print_cust()
            else:
                print("Wrong Password.")

        elif ans == 5:
            print("Thank you for your time!")
            sys.exit()  # closes the program

    except RuntimeError:
        print("Please check your input")
        print()
