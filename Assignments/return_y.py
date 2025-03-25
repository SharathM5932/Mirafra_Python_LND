"""Please enter the details to return the product.
Enter your name:Narendra
Enter the product name:Toy1
When did you purchase the product?
Please enter the date in mm/dd/yy format:08/01/23
Product:Toy1 will be collected from the delivered address and amount:499 will be returned to your account.
Thank you."""
from datetime import datetime,timedelta
from module1 import returnme

Sample={1:['Narendra','Toy1',499],
        2:['Sujara','Pink Saree',7500],
        3:['Shritan','T-Shirt',500]}
for x in range(100):
    print("Sample case {}".format(x+1))
    print("Please enter the details to return the product.")
    name=input("Enter your name:")
    for i in range(1,4):
        if name in Sample[i]:
            product=input("Enter the product name:")
            print("When did you purchase the product?")
            date=input("Please enter the date in mm/dd/yy format:")
            returnme(product,date,Sample[i][2])
            exit()
        else:
            product = input("Enter the product name:")
            print("When did you purchase the product?")
            date = input("Please enter the date in mm/dd/yy format:")
            print("You have not purchased that product recently with us.")
            print("Thank you")
            break

