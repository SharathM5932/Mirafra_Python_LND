import time
class bankaccount:
    def __init__(self,acc_no,acc_holder,pass_wrd,bal=0):
        self.acc_no=acc_no
        self.acc_holder=acc_holder
        self.pass_wrd=pass_wrd
        self.bal=bal
    def deposit(self,amount):
        if amount>0:
            self.bal+=amount
            print(f"deposited amount {amount}")
            print(f"balance={self.bal}")
        else:
            print(f"amount should be positive")

    def withdraw(self,amount):
        if 0<amount<=self.bal:
            self.bal-=amount
            print(f"withdrawn amount {amount}")
            print(f"balance={self.bal}")

        else:
            print(f"balance insufficient")

    def display(self):
        print(f"your balance = {self.bal}")


users = {
    '1001': bankaccount('1001', 'abhishek', 'pass123', 1000),
    '1002': bankaccount('1002', 'kalyan', 'pass456', 2000),
    '1003': bankaccount('1003', 'manish', 'pass789', 3000)
}
print("Good to see you here!")
print("\n")
acc_holder=input("enter full name:")
acc_no=input("enter account number: ")
pass_wrd=input('password:')

if acc_no in users and users[acc_no].pass_wrd == pass_wrd and users[acc_no].acc_holder==acc_holder:
    acc = users[acc_no]
    print(f"Welcome to BanK Mr/Mrs.{acc.acc_holder}\n")
    print('exit before leave')
else:
    print("Invalid account number or password \nIllegal user  ")
    exit()

while True:
    print("choose an option")
    print("1) Deposit")
    print("2) withdraw")
    print("3) check balance")
    print("4) exit")

    choice=input("select your choice")

    if choice=='1':
        acc.deposit(int(input("enter amount to be deposited: ")))
        time.sleep(2)
    elif choice=='2':
        acc.withdraw(int(input("enter anount to be withdrawn: ")))
        time.sleep(2)
    elif choice=='3':
        acc.display()
        time.sleep(2)
    elif choice=='4':
        print("exiting...")
        time.sleep(2)
        break
    else:
        print("Invalid input, try again")
