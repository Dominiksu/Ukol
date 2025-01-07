

class Bank_account:
    def __init__(self, owner, acc_number, acc_balance):
        self.owner = owner
        self.acc_number = acc_number
        self.acc_balance = acc_balance

    def salary(self, salary):
        self.acc_balance += salary
        


    def bills(self, prize):
        self.acc_balance -= prize


    def show_balance(self):
        print(self.acc_balance)

Account_01 = Bank_account('Karel', 444222442, 60000)
Account_02 = Bank_account('Pavla', 44554425, 50000)


Account_01.bills(44444)
Account_01.show_balance()

Account_02.salary(20000)
Account_02.show_balance()