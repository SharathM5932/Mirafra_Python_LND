def loyality_point(coupon,x):





i=1
while i<100:
    print("Sample case {}:".format(i))
    name=input("Please enter the customer name: ")

    print("Do you have coupon? type y or n")
    coupon=input()
    if coupon=='y':
        coupon_code=input("Please enter the coupon code: ")
    else:
        print("Enter the bill amount to be paid:{}".format(x))

    i+=1
