balance={100:{'Name':'Deepthi','pin':1234,'Net balance':0},
         101:{'Name':'Eva','pin':2345,'Net balance':100000},
         102:{'Name':'Raghavendra','pin':3456,'Net balance':110000},
         103:{'Name':'Sthuthi','pin':4567,'Net balance':85000},
         104:{'Name':'Sujay','pin':5678,'Net balance':50500}}
def balance_display(acc_no):
    if acc_no in balance:
        pin=int(input("Please enter the 4 digit pin: "))
        if pin==balance[acc_no]['pin']:
            print("Hi {}".format(balance[acc_no]['Name']))
            print("Your net balance is:{}".format(balance[acc_no]['Net balance']))
        else:
            print("Sorry Invalid Pin.")
    else:
        print("Entering wrong account no. Please try again.")
        print("Please visit our bank and create an account.")


i=1
while i<10:
    print("Sample case{}".format(i))
    acc_no=int(input("Please enter your Account no.: "))
    balance_display(acc_no)
    i+=1