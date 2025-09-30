class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._balance = float(initial_balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self._format(self._balance)}")

    def _format(self, value):
        v = float(value)
        if v.is_integer():
            return str(int(v))
        return f"{v:.2f}"
