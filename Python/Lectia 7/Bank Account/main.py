class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate= interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Your balance deposited with: {amount}USD")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(f"From your balance has been withdrawn: {amount}USD")
        else:
            print("Nu amagi MAIBU")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f"Credited with {interest}%")

    def history(self):
        for transaction in self.__transactions:
            print(transaction)


account = BankAccount(10000, 0.05)
account.deposit(2000)
account.withdraw(7500)
account.add_interest()
account.history()
