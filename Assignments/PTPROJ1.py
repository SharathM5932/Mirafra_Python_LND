import datetime

# menu function
def menu(data):
    print("MENU".center(44,"="))
    print("1.new user \n2.existing user\n3.Balance\n4.Deposit \n5.withdraw \n6.Transaction History\n7.exit")
    print("=" * 44)
    user_input = int(input("Enter your choice:"))
    match user_input:
        case 1:
            new_user(data)
        case 2:
            existing_user(data)
        case 3:
            balance(data)
        case 4:
            deposit(data)
        case 5:
            withdraw(data)
        case 6:
            transaction_details(data)
        case 7:
            exit()
        case _:
            print("enter correct input")
            main()


# function to create new user
def new_user(data):
    print("-"*44)
    account_no=int(input("Enter account no:"))
    # if account no exists
    if account_no in data:
        print('user account already exists')
    else:
        name=input("Enter user name:")
        password=input("Enter password:")

        init_balance=0.0
        data[account_no]=[name,password,init_balance,[]]#for transaction
        print("NAME:", data[account_no][0])
        print("ACCOUNT NO:", account_no)
        print("BALANCE:", data[account_no][2])

    print("-" * 44)

    menu(data)
# existing account
def existing_user(data):
    print("-"*44)
    account_no=int(input("enter account no:"))
    if account_no in data:
        password=input("enter password:")
        if data[account_no][1]==password:
            print("password matched")
            print("NAME:",data[account_no][0])


            print("ACCOUNT NO:", account_no)
            print("BALANCE:", data[account_no][2])
            menu(data)
        else:
            print("password unmatched")
            existing_user(data)

    else:
        print("Account not found. Create an account!")
        menu(data)
    print("-" * 44)


def balance(data):
    existing_user(data)
# deposit function
def deposit(data):
    print("-" * 44)
    account_no = int(input("enter account no:"))
    if account_no in data:
        password = input("enter password:")
        if data[account_no][1]==password:
            print("password matched")
            amount=float(input("Enter the amount to deposit:"))
            if amount<=0:
                print("enter amount correctly!")
                deposit(data)
            else:
                print('amount deposited to your account:', amount)

                # transaction function
                transaction(data,account_no,amount,"credited +")
                data[account_no][2] += amount

                print('current bank balance:', data[account_no][2])
            print("-" * 44)
            menu(data)
        else:
            print("password unmatched")
            print("-" * 44)
            deposit(data)
    else:
        print("account does not exists")
        print("-" * 44)
        menu(data)
# withdraw
def withdraw(data):
    print("-" * 44)
    account_no = int(input("enter account no:"))
    if account_no in data:
        password = input("enter password:")
        if data[account_no][1] == password:
            print("password matched")
            amount = float(input("Enter the amount to withdraw:"))
            if amount<=0:
                print("Enter amount greater than zero")
                withdraw(data)
            if amount>data[account_no][2]:
                print("Insufficient Balance")
                print('bank balance:', data[account_no][2])
                withdraw(data)
            else:
                print('amount withdrawn from your account:', amount)

                # transaction function
                transaction(data, account_no, amount, "debited -")

                data[account_no][2] -= amount
                print('current bank balance:', data[account_no][2])
                print("-" * 44)
                menu(data)
        else:
            print("password unmatched")
            print("-" * 44)
            withdraw(data)
    else:
        print("account does not exists")
        print("-" * 44)
        menu(data)


# Transaction history
def transaction(data,account_no,amount,action):
    data[account_no][3].append(action+str(amount)+" "+str(datetime.datetime.now()))
    pass


# Transaction details
def transaction_details(data):
    print("-" * 44)
    account_no = int(input("enter account no:"))
    if account_no in data:
        password = input("enter password:")
        if data[account_no][1] == password:
            print("password matched")
            if len(data[account_no][3])!=0:
                i = 1
                for trans in data[account_no][3]:
                    print(str(i) + "." + trans)
                    i += 1
            else:
                print("No Transaction History!")
            menu(data)
        else:
            print("password unmatched")
            print("-" * 44)
            transaction_details(data)
    else:
        print("account does not exists")
        print("-" * 44)
        menu(data)


# main function
def main():
    # dictionary to store all details
    data={}
    menu(data)


if __name__=="__main__":
    main()