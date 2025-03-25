customer = {'pin': 7890, 'balance': 2000, 'user_name': 'Radha'}
print("Welcome to ATM Machine")
pin = int(input("please enter your 4 digit pin: "))


def withdrawn_cash():
    while True:
        amount = int(input("Enter the amount to withdrawn"))
        if amount > customer['balance']:
            print("Insufficient balance")
        else:
            customer['balance'] = customer['balance'] - amount
            print(f"{amount} Rupees successfully withdrawn  your remaining balance is {customer['balance']} Rupees")
            return False


def balance_enquiry():
    print(f"Total balance {customer['balance']} Rupees")


def deposit():
    cash = int(input("enter the amount to deposit"))
    if cash <= 0:
        print("cant deposit")
    else:
        customer['balance'] = customer['balance'] + cash
        print(f"{cash} Rupees successfully deposit your balance is {customer['balance']} Rupees")


is_quit = False
if pin == customer['pin']:
    while is_quit == False:
        print("Enter 1 to withdrawn cash \n Enter 2 for Balance Enquiry \n Enter 3 for deposit \n Enter 4 to quit")
        case = int(input("Enter the value corresponding to the activity to do: "))
        if case == 1:
            withdrawn_cash()
        elif case == 2:
            balance_enquiry()
        elif case == 3:
            deposit()
        elif case == 4:
            is_quit = True
        else:
            print("Please enter a correct value ")
else:
    print("Entered wrong pin")