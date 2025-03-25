account={100:["Deepthi",1234,0],
         101:["Eva",2345,100000],
         102:['Raghavendra',3456,110000],
         103:['Sthuthi',4567,85000],
         104:['Sujay',5678,50500]}
while True:
    account_no = int(input("Enter the account number:"))
    if account_no in account:
        pin=int(input("Please enter the 4 digit pin:"))
        if pin ==account[account_no][1]:
            print("Hi {}".format(account[account_no][0]))
            print("Your net balance is: {}".format(account[account_no][2]))
        else:
            print("Sorry Invalid Pin.")
    else:
        print("Entering wrong account no. Please try again.\nPlease visit our bank and create an account.")
    print()
