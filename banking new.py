import os
from datetime import datetime

# ======= Configuration =======
PIN_CODE = "9390262117"  # Change this to your desired PIN
ACCOUNT_FILE = "account.txt"

# ======= Authentication =======
def authenticate():
    print("*********************")
    entered_pin = input(" Enter your 4-digit PIN: ")
    print("*********************")
    if entered_pin == PIN_CODE:
        print(" Access granted")
        return True
    else:
        print(" Incorrect PIN. Access denied.")
        return False

# ======= Balance Functions =======
def load_balance():
    if not os.path.exists(ACCOUNT_FILE):
        return 0.0
    with open(ACCOUNT_FILE, "r") as file:
        lines = file.readlines()
        for line in reversed(lines):
            if line.startswith("BALANCE:"):
                return float(line.strip().split(":")[1])
    return 0.0

def save_transaction(action, amount, balance):
    with open(ACCOUNT_FILE, "a") as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{now} - {action} {amount:.2f} | Balance: {balance:.2f}\n")
        file.write(f"BALANCE:{balance:.2f}\n")

# ======= Banking Actions =======
def show_balance(balance):
    print("*********************")
    print(f" Your balance is: {balance:.2f}")
    print("*********************")

def deposit(balance):
    try:
        amount = float(input(" Enter amount to deposit: "))
        if amount <= 0:
            print(" Invalid amount. Must be more than 0.")
            return balance
        balance += amount
        save_transaction("Deposited", amount, balance)
        print(f" Deposited {amount:.2f}")
    except ValueError:
        print(" Please enter a valid number.")
    return balance

def withdraw(balance):
    try:
        amount = float(input(" Enter amount to withdraw: "))
        if amount <= 0:
            print(" Invalid amount. Must be more than 0.")
        elif amount > balance:
            print(" Insufficient funds.")
        else:
            balance -= amount
            save_transaction("Withdrawn", amount, balance)
            print(f" Withdrawn {amount:.2f}")
    except ValueError:
        print(" Please enter a valid number.")
    return balance

def show_transaction_history():
    print("*********************")
    print(" Transaction History:")
    print("*********************")
    if not os.path.exists(ACCOUNT_FILE):
        print("No transactions found.")
        return
    with open(ACCOUNT_FILE, "r") as file:
        lines = file.readlines()
        for line in lines:
            if not line.startswith("BALANCE:"):
                print(line.strip())

# ======= Main Program =======
def main():
    if not authenticate():
        return

    balance = load_balance()
    running = True

    while running:
        print("\n*********************")
        print(" Banking Menu")
        print("*********************")
        print(" Show Balance")
        print("  Deposit")
        print(" Withdraw")
        print("  Show Transaction History")
        print("  Exit")
        print("*********************")
        choice = input(" Enter your choice (1-5): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            show_transaction_history()
        elif choice == '5':
            print(" Thank you! Visit again.")
            running = False
        else:
            print(" Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
