coupon=['CDEC01','ONEJAN02','2234150']
print('Welcome to online shopping.')
print('your cart is not empty.')
amount=1500
print(f'You have to pay Rs. {amount}/-')
choice=input('Do you have coupon? type y or n:')
if choice=='y':
    code=input('Please enter the coupon code:')
    if code in coupon:
        if code==coupon[0]:
            amount-=500
            print(f'successfully applied the coupon code. Please pay {amount}/-')
        elif code==coupon[1]:
            amount=int(amount/2)
            print(f'successfully applied the coupon code. Please pay {amount}/-')
        elif code==coupon[2]:
            print('successfully applied the coupon code.')
            print(f'Congratulations! You got 1000 loyalty points for shopping with us. Please pay {amount}/-')
    else:print('coupon code is not valid')
else:print(f'Please pay Rs. {amount}/-')

