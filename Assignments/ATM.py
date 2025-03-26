def show_balance(balance):
    print(f"your balance is {balance:.2f}")
def deposit():
    amount=float(input('enter the amount to deposit'))
    if amount<0:
        print("not a valid amount")
    else:
        return amount
def withdraw(balance):
    amount=float(input('enter the amount to withdraw'))
    if amount>balance:
        print("insufficient fund")

    elif amount<0:
        print("amount must be greater than 0")

    else:
        return amount
def main():
    balance = 0
    is_running = True
    password = 1234
    pin = int(input('enter the pin'))
    if pin==password:
        while is_running:
            print("1.show Balance")
            print("2.Deposit")
            print("3.withdraw")
            print("4.exit")
            choice = input('enter the choice 1 t0 4:')
            if choice == '1':
                show_balance(balance)
            elif choice == '2':
                balance += deposit()
            elif choice == '3':
                balance -= withdraw(balance)
            elif choice == '4':
                is_running = False
            # else:
            #     print("there is no valid choice")
        print("Thank You")
main()
