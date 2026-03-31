# Q4. Bank Account Management using class and parameterized constructor

class BankAccount:
    def __init__(self, acc_no, holder, balance):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account No:", self.acc_no)
        print("Holder:", self.holder)
        print("Balance:", self.balance)


acc = BankAccount(12345, "Pallavi", 10000)
acc.deposit(2000)
acc.withdraw(5000)
acc.display()