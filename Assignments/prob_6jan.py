class Bank_ATM:
    def __init__(self,password,balance,cu_id):
        self.password=password
        self.balance=balance
        self.cu_id=cu_id
    stop=True


    def deposit(self,amount):
        if self.cu_id==460743421 and password==1111 or password==new_pass :
            self.balance+=amount
            print("You deposited {}rs Successfully.".format(amount))
            print("Your Account Balance is {}rs.".format(self.balance))
        else:
            print("Invalid login")


    def withdraw(self,amt):
        if self.cu_id==460743421 and password==1111 or password==new_pass:
             if self.balance>amt:
                 self.balance-=amt
                 print("You withdrawn {}rs Successfully.".format(amt))
                 print("Your account Balance is {}rs.".format(self.balance))
             else:
                 print("insufficient balance")
        else:
            print("Invalid login")


    def check_balance(self):
        if self.cu_id == 460743421 and self.password == 1111 or self.password == new_pass:
            print("Your account balance is {}rs.".format(self.balance))
        else:
            print("Invalid Login Details.")
    def change_password(self,new_pass):
        if self.cu_id==460743421:
            self.password=new_pass
            print("Successfully Changed the Password")
        else:
            print("Wrong Customer Id")


stop=False
print("#############WELCOME#############")
print("---------------------------------")
cu_id=int(input("Enter the customer ID:"))
password=int(input("Enter the 4 digit PIN:"))
print("---------------------------------")
ac_1=Bank_ATM(password,0,cu_id)
if cu_id==460743421 and password==1111:
    while stop==False:
        choice = int(input("""
                 1.Deposit
                 2.Withdraw
                 3.Check Balance
                 4.Forgot Password
                 5.Logout
                 """))
        if choice==1:
             amt=int(input("How much do you want to deposit:"))
             if amt>0:
                ac_1.deposit(amt)
                print("---------------------------------")
                continue
             else:
                print("Please enter positive amount to deposit")
        elif choice==2:
                amt_1= int(input("How much do you want to withdraw:"))
                if amt_1 > 0:
                    ac_1.withdraw(amt_1)
                    print("---------------------------------")
                else:
                    print("Please enter positive amount to withdraw")
        elif choice==3:
                ac_1.check_balance()
                print("---------------------------------")
        elif choice==4:
                id=int(input("Enter your customer id:"))
                if id==cu_id:
                    new_pass=input("Enter New password:")
                    ac_1.change_password(new_pass)
                    print("---------------------------------")
                else:
                    print("Invalid data")
        elif choice==5:
               stop==True
               print("Logout Successfully.")
               exit()
        else:
                stop=True
                print("Invalid Choice")

















