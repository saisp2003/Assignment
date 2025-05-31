#Bank account with deposit and withdrawal

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def display_balance(self):
        print(f"Current balance: Rs.{self.balance:.2f}")  
# Example usage
account = BankAccount(100)  
account.display_balance()  
account.deposit(50)  
account.display_balance()  
