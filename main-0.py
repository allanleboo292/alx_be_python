import sys
from bank_account import BankAccount

def main():
    # Initialize the bank account with a starting balance of $100
    account = BankAccount(100)

    # Check if at least one command-line argument is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the first argument into command and amount (if provided)
    command_input = sys.argv[1]
    if ':' in command_input:
        command, param = command_input.split(':', 1)
    else:
        command = command_input
        param = None

    # Convert the amount to a float if it's provided
    amount = float(param) if param else None

    # Execute the corresponding method based on the command
    if command.lower() == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command.lower() == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command.lower() == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

if __name__ == "__main__":
    main()

