# import scenario
# def main():
#     print("Please enter the details to return the product.")
#     name=input("Enter your name:")
#     product=input("Enter the product name:")
#     print("When did you purchase the product?")
#     date=input("Please enter the date in mm/dd/yy format:")
#     print(scenario.returnme(name,product,date))
#     print("Thank you.")
#
# if __name__=="__main__":
#     main()

# scenario2======================
class Bank:
    def __init__(self):
        self.data={100:['Deepthi',1234,0],
          101:['Eva',2345,100000],
          102:['Raghavendra',3456,110000],
          103:['Sthuthi',4567,85000],
          104:['Sujay',5678,50500]}


    def check_acc(self,acc_no):
        if acc_no in self.data:
            return True
        return False
    def check_pin(self,pin,acc_no):
        if pin in self.data[acc_no]:
            return [self.data[acc_no][0],self.data[acc_no][2]]
        else:
            return []
    def start(self):
        acc_no = int(input("Please enter your Account no.:"))
        if self.check_acc(acc_no):
            pin = int(input("Please enter the 4 digit pin:"))
            result = self.check_pin(pin, acc_no)
            if len(result) != 0:
                print(f"Hi {result[0]}")
                print(f"Your net balance is: {result[1]}")
            else:
                print("Sorry Invalid Pin.")

        else:
            print('''Entering wrong account no. Please try again.\nPlease visit our bank and create an account.
        ''')

b=Bank()
b.start()