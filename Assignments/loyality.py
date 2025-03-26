data={'Sajid':120,'Roopesh':85, 'Koushik':50, 'Lakshmi':64, 'Sathvik':12}
name=input('Please enter the customer name:')
if name  in data.keys():
    print(f'Customer Name:{name}')
else:print('New customer')
choice=input('Do the customer has the coupon? Type y or n:')
cp=0
if choice=='y':
    code=input('Please enter the coupon code:')
    if code=='123476':
        cb=20
    else:print("Wrong coupon code, loyality points won't get added")
amount=int(input('Enter the bill amount to be paid:'))
b=round(amount/100)
lp=b+cp
if name in data.keys():
    lp=b+cp+data[name]
if lp>=100:
    print(f'Congratulations! you won Rs. 100 cash back. You have to pay Rs.:{amount-100},And remaining loyalty points in your account is:{lp-100}')
else:print(f'You have, {lp} loyalty points in your account. Please pay Rs.:{amount},Thank you.')



