import datetime as d
product_code=[[1,'soap',12,d.date(2022,3,14)],[2,'shampoo',6,d.date(2022,3,14)],[3,'Toothpaste',7,d.date(2022,12,2)],[4,'Ready juice',2,d.date(2022,8,11)],[5,'chips',1,d.date(2022,11,20)]]
def exp_date(p_code,a):
   for i in range(1):
            if p_code==1:
                if a<=d.date(2023,3,14):
                    print("Soap is Good to sale")
                else:
                    print("Product Expired")
            elif p_code==2:
                if a<=d.date(2022,9,14):
                    print(" shampoo is Good to sale")
                else:
                    print("Product expired")
            elif p_code==3:
                if a<=d.date(2022,9,12):
                    print("Toothpaste is Good to sale")
                else:
                    print("Product expired")
            elif p_code==4:
                if a<=d.date(2022,10,11):
                    print("Ready Juice is Good to sale")
                else:
                    print("Product expired")
            elif p_code==5:
                if a<=d.date(2022,12,20):
                    print("chips are Good to sale")
                else:
                    print("Product expired")
            else:
                print("Invalid Product Code.")

while True:
    print("WELCOME TO GANESH SUPER MARKET INSPECTION PORTAL")
    print("================================================")
    print("Enter the product Code")
    a=d.date(2023,1,12)
    p_code=int(input())
    print("Today's date is: {}".format(a))
    exp_date(p_code,a)
