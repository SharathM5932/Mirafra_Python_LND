class bank_account:
    def __init__(self, acc_name, password, balance=0):
        self.acc_name = acc_name
        self.balance = balance
        self.password = password


    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print('Negative cannot be deposited')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient balance')

    def get_balance(self):
        print("Balance is",self.balance)

name = input('Enter your name:')
password = int(input('Enter the password:'))
person1 = bank_account(name, password)
data={"abc":1234,'xyz':5678}

if name in list(data.keys()):

    if (name,password) in list(data.items()):
        while True:
            print('Enter 1 to deposit')
            print('Enter 2 to withdraw')
            print('Enter 3 to get balance')
            print('Enter 4 to exit')

            choice = int(input())
            if choice == 1:
                print('Enter the amount to be deposited')
                amount = int(input())
                person1.deposit(amount)
            elif choice == 2:
                print('Enter the amount to be withdraw')
                amount = int(input())
                person1.withdraw(amount)
            elif choice == 3:
                person1.get_balance()
            elif choice == 4:
                break
    else:print('wrong password')
else:print('user name not found')