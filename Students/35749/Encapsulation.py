class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)