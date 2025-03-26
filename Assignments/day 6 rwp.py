print("Please fill the details to sign in.")
Name=input("Full Name:")
print("Delivery address:")
Add=''
Add=Add+input("Line 1:")
Add=Add+input("Line 2:")
Add=Add+input("Line 3:")
email=input("email ID:")
while True:
    if '@' in email:
        s=email.split('@')
        if len(s)==2 and '.' in s[1]:
            break
        else:
            email = input("Please enter a valid email ID:")
    else:
        email=input("Please enter a valid email ID:")
card=input("Card no.:")
while True:
    if card.isnumeric() and len(card)==16:
        break
    else:
        card=input("Enter 16 digits card no.:")
gst=input("GST no.:")
while True:
    a=sum(i.isdigit() for i in gst)
    b=sum(i.isalpha() for i in gst)
    if a==8 and b==7:
        break
    else:
        gst=input("Enter a valid GST no.:")
print("Thank you.")

#--------------------------------------------------------------------------------------


inpt=input("""Welcome to online shopping.
your cart is not empty.
You have to pay Rs. 1500/-
Do you have coupon? type y or n""")
if inpt=='n':
    print(f"Please pay Rs. {n}/-")
else:
    while True:
        code = input("Please enter the coupon code:")
        if code == 'CDEC01':
            print("successfully applied the coupon code. Please pay 1000/-")
            break
        elif code == 'ONEJAN02':
            print("successfully applied the coupon code. Please pay 750/-")
            break
        elif code == '2234150':
            print("successfully applied the coupon code.\nCongratulations! You got 1000 loyalty points for shopping with us. Please pay 1500/-")
            break
        else:
            code = input("Enter the valid code")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

def find(prod_dict,code):
    if prod_dict[code][0]>0:
        if prod_dict[code][2]==True:
            print("Product Type:", prod_dict[code][1])
            print("Product Price:", prod_dict[code][3] , "+ 600/- Rs. Delivery charge.")
            print("Please pay Rs.",prod_dict[code][3]+600)
            print("The product will be delivered to your home.")
        else:
            print("Product Type:", prod_dict[code][1])
            print("Price:", prod_dict[code][3])
            print(f"You can collect the product in the ground floor, Bay: {prod_dict[code][4][0]} Row: {prod_dict[code][4][1]} Column: {prod_dict[code][4][2]}")
    else:
        print("Product Type:",prod_dict[code][1])
        print("Sorry! Out of stock")
prod_dict={
    "pdcR012":[0,"Shelf",True,50000],
    "pdcc01":[1,"Chair",False,1500,[1,1,2]],
    "pdcs11":[1,"Sofa",True,60000]
}
code=input("Please enter the product code:")
if code in prod_dict:
    find(prod_dict,code)
else:
    print("Please enter a valid product code.")






