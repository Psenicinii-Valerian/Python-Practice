class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount_of_money):
        if self.balance >= amount_of_money:
            self.balance -= amount_of_money
            print(f"You've successfully withdrawed {amount_of_money} lei!")
        else:
            print("OH NOOO! Don't try to fraud MAIB! Withdrawal has been canceled")

    def deposit(self, amount_of_money):
        self.balance += amount_of_money
        print(f"You've successfully added {amount_of_money} lei to your bank account!")

    def display_balance(self):
        print(f"Your current balance = {self.balance} lei")
