import sys
from bank_account import BankAccount

def format_amount(value):
    v = float(value)
    if v.is_integer():
        return str(int(v))
    return f"{v:.2f}"

def main():
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    part = sys.argv[1]
    if ':' in part:
        command, amt_str = part.split(':', 1)
        amt_str = amt_str.strip()
    else:
        command = part
        amt_str = None

    command = command.lower()
    amount = None
    if amt_str:
        try:
            amount = float(amt_str)
        except ValueError:
            print("Invalid amount.")
            sys.exit(1)

    if command == "deposit":
        if amount is None:
            print("Usage: python main-0.py deposit:<amount>")
            sys.exit(1)
        if amount <= 0:
            print("Invalid amount.")
            sys.exit(1)
        account.deposit(amount)
        print(f"Deposited: ${format_amount(amount)}")

    elif command == "withdraw":
        if amount is None:
            print("Usage: python main-0.py withdraw:<amount>")
            sys.exit(1)
        if amount <= 0:
            print("Invalid amount.")
            sys.exit(1)
        if account.withdraw(amount):
            print(f"Withdrew: ${format_amount(amount)}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
