# scenario1
'''name=input("Full Name:")
print("Delivery address:")
line1=input("Line 1:")
line2=input("Line 2:")
line3=input("Line 3:")
email = input("email ID:")
value=r".*@.*\.com$"
import re
flag=True
while flag==True:
    if re.match(value,email):
        flag=False
    else:
        email=input("Please enter a valid email ID:")
card=input("Card no:")
# print(len(card))
flag=True
value1=r"^[0-9]{16}$"
while flag==True:
    if re.match(value1,card):
        flag=False
    else:
        email=input("Enter 16 digits card no.:")
gst=input("GST no.:")
value3=r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][0-9][A-Z][0-9]$'
flag=True
while flag==True:
    if re.match(value3,gst):
        flag=False
    else:
        gst=input("Enter a valid GST no.:")
print("Thank you")'''

# scenario2===========================]
'''def find(prod_dict,code):
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
    print("Please enter a valid product code.")'''


# scenario3========================
str1='''Welcome to online shopping.
your cart is not empty.
You have to pay Rs. 1500/-'''
print(str1)
dict3={'CDEC01':["sub",500,False],
       'ONEJAN02':["div",2,False],
       '2234150':[0,0,True]}
choice=input("Do you have coupon? type y or n:")
match choice:
    case 'y':
        code=input("Please enter the coupon code:").upper()
        amount=1500
        if dict3[code][2]==True:
            str2='''successfully applied the coupon code.
Congratulations! You got 1000 loyalty points for shopping with us. Please pay 1500/-'''
            print(str2)
        else:
            if dict3[code][0]=="sub":
                amount-=dict3[code][1]
            elif dict3[code][0]=="div":
                amount/=dict3[code][1]
            print(f"successfully applied the coupon code. Please pay {amount}/-")
    case 'n':
        print("Please pay Rs. 1500/-")
    case _:
        exit()












