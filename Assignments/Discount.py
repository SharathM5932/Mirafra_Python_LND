#Discount coupon
#Ravi has an online sweets store called ‘XYZ’. He wants to announce discount on the occasions of Christmas and new year.
# He has already distributed coupon codes amongst his customers. Please help him by writing piece of code which will be reducing
# the payable amount by the customer only if the coupon code is correct. Please note the coupon codes are case sensitive.
#Descriptions of coupon codes:
#1.	Please consider the payable amount by the customer  is Rs. 1500/-.
#2.	If the coupon code is 'CDEC01' then reduce Rs. 500/- from payable amount.
#3.	If the coupon code is 'ONEJAN02' then reduce half of the price from payable amount.
#4.	If the coupon code is '2234150' then display the message that the customer has earned 1000 loyalty points and don’t reduce any amount  from payable.

def discount_code(coupon_code,x):
    if coupon_code=="CDEC01":
        x-=500
        print("successfully applied the coupon code. Please pay {}".format(x))
    elif coupon_code=="ONEJAN02":
        x//=2
        print("successfully applied the coupon code. Please pay {}".format(x))
    elif coupon_code=="2234150":
        print("successfully applied the coupon code.")
        print("Congratulations! You got 1000 loyalty points for shopping with us. Please pay {}".format(x))
    else:
        print("Please pay Rs.{}".format(x))

i=1
while i<100:
    print("Sample case {}:".format(i))
    print("Welcome to online shopping.")
    print("your cart is not empty.")
    x=1500
    print("You have to pay Rs. 1500/-")
    print("Do you have coupon? type y or n")
    coupon=input()
    if coupon=='y':
        coupon_code=input("Please enter the coupon code: ")
        discount_code(coupon_code,x)
    else:
        print("Please pay Rs.{}".format(x))

    i+=1

