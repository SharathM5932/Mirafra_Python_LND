from module1 import returnme
print("Please enter the details to return the product.")
data={'Narendra':['Toy1',499],
      'Sujara':['Pink Saree',7500],
      'Shritan':['T-shirt',500]}
i=1
while(i<10):
      print("Sample Case:{}".format(i))
      name=input("Enter your name:")
      if name in data:
                  product_name=input("Enter the product name:")
                  print("When did you purchase the product?")
                  date=input("Please enter the date in mm/dd/yy format:")
                  a=returnme(date)
                  if a==1:
                        print("Product:{} will be collected from the delivered address and amount:{} will be returned to your account.".format(data[name][0],data[name][1]))
                  else:
                        print("Sorry! the product cannot be returned\nThank you.")

      else:
                  product_name = input("Enter the product name:")
                  print("When did you purchase the product?")
                  date = input("Please enter the date in mm/dd/yy format:")
                  print("You have not purchased that product recently with us.\nThank you.")
      i+=1

