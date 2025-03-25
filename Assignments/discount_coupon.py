"""Discount coupon
Ravi has an online sweets store called ‘XYZ’.
He wants to announce discount on the occasions of Christmas and new year.
He has already distributed coupon codes amongst his customers.
Please help him by writing piece of code which will be reducing
the payable amount by the customer only if the coupon code is correct.
Please note the coupon codes are case sensitive.
 Descriptions of coupon codes:
1.	Please consider the payable amount by the customer  is Rs. 1500/-.
2.	If the coupon code is 'CDEC01' then reduce Rs. 500/- from payable amount.
3.	If the coupon code is 'ONEJAN02' then reduce half of the price from payable amount.
4.	If the coupon code is '2234150' then display the message that the customer has earned 1000 loyalty points and don’t reduce any amount  from payable.
"""
def discount(s,a):
    if s=="CDEC01":
        a-=500
        print("successfully applied the coupon code. Please pay {}/-".format(a))
    elif s=="ONEJAN02":
        a//=2
        print("successfully applied the coupon code. Please pay {}/-".format(a))
    elif s=="2234150":
        print("Congratulations! You got 1000 loyalty points for shopping with us. Please pay {}/-".format(a))
    else:
        print("Invalid Coupon Code")
        print("Please pay Rs.{}".format(a))

i=1
while(i<100000000000000):
    print("Sample Case {}:".format(i))
    print("WELCOME TO ONLINE SHOPPING")
    print("Your cart is not empty.")
    a=1500
    print("You have to pay Rs. 1500/-")
    print("Do you have a coupon?")
    coupon=input()
    if coupon=='y':
        s=input("Enter the Coupon Code:")
        discount(s,a)
        print()
    elif coupon=='n':
        print("Please pay Rs.{}".format(a))
    i+=1
