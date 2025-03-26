def authenticate(pin):
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("PIN accepted!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts remaining.")
    print("Too many incorrect attempts. Access denied.")
    return False
def display_menu():
    print("""\nATM Menu:
    1. Withdraw
    2. Balance Enquiry
    3. Change PIN
    4. Deposit
    5. Recent Transactions
    6. Exit""")
def withdraw(balance,transaction_history):
    amount=float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance-=amount
        transaction_history.append(f"Withdrawal: {amount}")
        print(f"Withdrawal successful! Your new balance is: {balance}")
    return balance, transaction_history
def balance_enquiry(balance):
    print(f"Your current balance is: {balance}")
def change_pin(pin):
    new_pin = input("Enter your new 4-digit PIN: ")
    print("PIN changed successfully!")
    return new_pin
def deposit(balance, transaction_history):
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    transaction_history.append(f"Deposit: {amount}")
    print(f"Deposit successful! Your new balance is: {balance}")
    return balance, transaction_history
def recent_transactions(transaction_history):
    print("\nRecent Transactions:")
    if not transaction_history:
        print("No recent transactions.")
    else:
        for transaction in transaction_history[-5:]:
            print(transaction)
def atm_program():
    pin = "1234"
    balance = 1000
    transaction_history = []

    if not authenticate(pin):
        return
    while True:
        display_menu()
        choice = input("Please choose an option (1-6): ")
        if choice == '1':
            balance,transaction_history = withdraw(balance,transaction_history)
        elif choice == '2':
            balance_enquiry(balance)
        elif choice == '3':
            pin = change_pin(pin)
        elif choice == '4':
            balance,transaction_history = deposit(balance,transaction_history)
        elif choice == '5':
            recent_transactions(transaction_history)
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
atm_program()