loyalty_points_db = {
    'Sajid': 120,
    'Roopesh': 85,
    'Koushik': 50,
    'Lakshmi': 64,
    'Sathvik': 12
}
def cal_loyality(bill, code):
    points_bill = bill/100
    if code=='123476':
        points_bill+=20
    elif code==0:
        points_bill+=0
    else:
        print("Wrong coupon code. Loyalty points won't get added.")
        points_bill+=0
    return points_bill


name=input("Please enter the customer name: ").capitalize()
if name not in loyalty_points_db:
    print("New Customer")
    loyalty_points=0
else:
    print('Customer name:', name)
    loyalty_points = int(loyalty_points_db[name])

coupon=input("Do the customer has the coupon? Type y or n:").lower()
if coupon=='y':
    code=input("Please enter the coupon code: ")
elif coupon=='n':
    code=0
else:
    code = 0
    print("No coupon existing")

bill=float(input("Enter the bill amount to be paid: "))
new_point = cal_loyality(bill, code)
total=loyalty_points+new_point

if total >= 100:
    cashback = 100
    total -= cashback
    total=round(total)
    print(f"Congratulations! you won Rs. {cashback} cash back. You have to pay Rs.:, {bill-100}, \nAnd remaining loyalty points in your account is: {total}")
else:
    cashback=0
    print('You have', {total}, 'loyalty points in your account. Please pay Rs.:', {bill}, 'Thank you.')
