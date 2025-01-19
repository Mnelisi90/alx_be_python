class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient."""
        if amount > self.__account_balance:
            print("Insufficient funds.")
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current balance: ${self.__account_balance:.2f}")

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands:")
        print("  deposit:<amount> - Deposit the specified amount.")
        print("  withdraw:<amount> - Withdraw the specified amount.")
        print("  display - Display the current balance.")
        sys.exit(1)

    try:
        # Parse the command and amount
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None

        # Execute the command
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")

    except ValueError:
        print("Invalid format. Please use <command>:<amount> for deposit and withdraw.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()