# creating class
class Bank_account:
    # creating constructor(responsible for creating objects)
    def __init__(self, id, name, amount):
        self.id = id
        self.name = name
        self.amount = amount

    # creating deposit function
    def deposit_money(self, amt): # This will be responsible for adding money to the acc
        self.amount += amt

    # creating deposit function
    def withdraw_money(self, amt): # this will be responsible for removing money from acc
        self.amount -= amt

    # showing customer details
    def print_cust(self):
        print(self.id, self.name, self.amount)
