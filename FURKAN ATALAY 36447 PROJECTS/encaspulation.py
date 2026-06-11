# --- ENCAPSULATION EXAMPLE ---

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # Private attribute (hidden from outside world)
        self.__balance = balance

        # Public method to access private data safely (Getter)

    def get_balance(self):
        return self.__balance

    # Public method to modify private data safely (Setter)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")


# --- TESTING ENCAPSULATION ---
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)

    # account.__balance = 50000  # ERROR: Cannot change directly!
    account.deposit(500)  # Output: Deposited: $500. New Balance: $1500
    print(f"Account Balance: ${account.get_balance()}")  # Output: Account Balance: $1500