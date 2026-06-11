# Encapsulation = hiding internal data and protecting it from direct access

class BankAccount:
    def __init__(self, balance):
        # private variable (cannot be accessed directly outside class)
        self.__balance = balance

    # public method to access private data safely
    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

# we cannot access __balance directly, only through method
print(account.get_balance())