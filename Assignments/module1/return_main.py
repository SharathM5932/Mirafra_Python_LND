from return7days import return_prod

name=input("Enter your name:").capitalize()
prod_name=input("Enter the product name:").capitalize()
date_prod=input("When did you purchase the product?\nPlease enter the date in mm/dd/yy format:")
return_prod(name,prod_name,date_prod)
print("Thank you")