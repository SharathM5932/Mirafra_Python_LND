from module1 import returnme
name=input("Enter your name:")
product=input("Enter the product name:")
print("When did you purchase the product?")
d=input("Please enter the date in mm/dd/yy format:")
op=returnme(name,product,d)
print(op)
