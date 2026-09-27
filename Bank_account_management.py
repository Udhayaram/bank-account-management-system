"""
Bank Account Management System
--------------------------------
A console-based banking application built using core Python concepts:
Functions, Loops, Conditions, Lists, Dictionaries, Operators,
Input Validation, and Exception Handling.

Author: (Your Name)
"""

import datetime

# ------------------------------------------------------------------
# Data storage
# ------------------------------------------------------------------
# accounts is a dictionary of dictionaries:
# {
#   1001: {
#       "name": "Udhayaram",
#       "balance": 15000,
#       "transactions": [ "Deposit: +2000 | Balance: 17000", ... ]
#   }
# }
accounts = {}
next_account_number = 1001  # auto-incrementing account number


# ------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------
def format_currency(amount):
    """Format a number as Indian Rupee currency string."""
    return f"₹{amount:,.2f}"


def get_valid_amount(prompt):
    """Repeatedly ask the user for a valid positive amount."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_valid_account_number():
    """Ask for an account number and validate it exists."""
    while True:
        try:
            acc_no = int(input("Enter Account Number: "))
            if acc_no not in accounts:
                print("Account not found. Please try again.")
                continue
            return acc_no
        except ValueError:
            print("Invalid input. Account number must be numeric.")


def log_transaction(acc_no, description):
    """Add a timestamped entry to the account's transaction history."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc_no]["transactions"].append(f"[{timestamp}] {description}")


# ------------------------------------------------------------------
# Core features
# ------------------------------------------------------------------
def create_account():
    global next_account_number

    name = input("Enter Account Holder Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter Account Holder Name: ").strip()

    initial_deposit = get_valid_amount("Enter Initial Deposit Amount: ₹")

    acc_no = next_account_number
    accounts[acc_no] = {
        "name": name,
        "balance": initial_deposit,
        "transactions": []
    }
    log_transaction(acc_no, f"Account created with initial deposit {format_currency(initial_deposit)}")

    next_account_number += 1

    print(f"\nAccount created successfully!")
    print(f"Account Number: {acc_no}")
    print(f"Name: {name}")
    print(f"Balance: {format_currency(initial_deposit)}\n")


def deposit_money():
    if not accounts:
        print("No accounts exist yet. Please create an account first.\n")
        return

    acc_no = get_valid_account_number()
    amount = get_valid_amount("Enter Deposit Amount: ₹")

    accounts[acc_no]["balance"] += amount
    log_transaction(acc_no, f"Deposit: +{format_currency(amount)} | New Balance: {format_currency(accounts[acc_no]['balance'])}")

    print(f"\nDeposit successful!")
    print(f"New Balance: {format_currency(accounts[acc_no]['balance'])}\n")


def withdraw_money():
    if not accounts:
        print("No accounts exist yet. Please create an account first.\n")
        return

    acc_no = get_valid_account_number()
    amount = get_valid_amount("Enter Withdrawal Amount: ₹")

    try:
        if amount > accounts[acc_no]["balance"]:
            raise ValueError("Insufficient balance for this withdrawal.")

        accounts[acc_no]["balance"] -= amount
        log_transaction(acc_no, f"Withdraw: -{format_currency(amount)} | New Balance: {format_currency(accounts[acc_no]['balance'])}")

        print(f"\nWithdrawal successful!")
        print(f"New Balance: {format_currency(accounts[acc_no]['balance'])}\n")

    except ValueError as e:
        print(f"\nTransaction failed: {e}\n")


def check_balance():
    if not accounts:
        print("No accounts exist yet. Please create an account first.\n")
        return

    acc_no = get_valid_account_number()
    print(f"\nCurrent Balance: {format_currency(accounts[acc_no]['balance'])}\n")


def account_details():
    if not accounts:
        print("No accounts exist yet. Please create an account first.\n")
        return

    acc_no = get_valid_account_number()
    account = accounts[acc_no]

    print("\n--- Account Details ---")
    print(f"Account Number : {acc_no}")
    print(f"Name           : {account['name']}")
    print(f"Balance        : {format_currency(account['balance'])}")
    print(f"Total Transactions: {len(account['transactions'])}\n")


def transaction_history():
    if not accounts:
        print("No accounts exist yet. Please create an account first.\n")
        return

    acc_no = get_valid_account_number()
    transactions = accounts[acc_no]["transactions"]

    print(f"\n--- Transaction History for Account {acc_no} ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)
    print()


# ------------------------------------------------------------------
# Menu system
# ------------------------------------------------------------------
def show_menu():
    print("=" * 40)
    print("     BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Transaction History")
    print("7. Exit")
    print("=" * 40)


def main():
    menu_actions = {
        "1": create_account,
        "2": deposit_money,
        "3": withdraw_money,
        "4": check_balance,
        "5": account_details,
        "6": transaction_history,
    }

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("\nThank you for using the Bank Account Management System. Goodbye!")
            break
        elif choice in menu_actions:
            menu_actions[choice]()
        else:
            print("\nInvalid choice. Please select a number between 1 and 7.\n")


if __name__ == "__main__":
    main()
