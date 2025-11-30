class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance formatted to 2 decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")


