from datetime import datetime
class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance
    def get_transaction_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited: ", amount)
        print("Transaction time: ", self.get_transaction_time())
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn: ", amount)
            print("Transaction time: ", self.get_transaction_time())
        else:
            print("Insufficient balance.")
    def check_balance(self):
        print("account_holder: ", self.acc_holder)
        print("current balance: ", self.balance)
        print("Transaction time: ", self.get_transaction_time())

account = BankAccount("Rakesh", 200000)
account.deposit(2000)
account.check_balance()
account.withdraw(49999)
account.check_balance()