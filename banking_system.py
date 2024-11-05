# Define the BankAccount class
class BankAccount:
    # Constructor to initialize account number, account holder name, and balance
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to display account information
    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Example usage
# Creating an account
account1 = BankAccount("123456789", "Francis Mwangi", 1000.0)

# Display account information
account1.display_info()

# Deposit money
account1.deposit(500)

# Withdraw money
account1.withdraw(200)

# Withdraw with insufficient funds
account1.withdraw(2000)

# Display account information again
account1.display_info()
