def display():
    print('''Welcome to our shop.
    The list items:
    Product:Price in Rs.
    Rava:70
    Rice:55
    Sugar:50
    Toor dal:150
    Wheat flour:55
    For your surprise we have offers going on:
    Buy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour.''')

def sales():
    q = input('Enter the item name:')
    q = q.lower()
    if q not in ['rava','rice','sugar','toor dal','wheat flour']:
        print('Enter the item name present in our shop and try again.')
        exit()

    try:
        r = int(input('Enter the quantity in KGs:'))
    except ValueError:
        print('Please enter an integer value.')
    else:
        if q == 'sugar' and r >= 2:
            if r == 5:
                n = 150
            else:
                n = r * 25.0
        elif q == 'wheat flour' and r >= 2:
            n = r * 55 / 2
        elif q == 'rava':
            n = r * 70
        elif q == 'rice':
            n = r * 55
        elif q == 'toor dal':
            n = r * 150
        else:
            print('Item is Not Present')
        print(f"you have asked for {r}kg of {q}")
        print(f"Please pay Rs.:{n}")
# li = [('rava', 70), ('rice', 55), ('sugar', 50), ('toor dal', 150), ('wheat flour', 55)]
display()
sales()

#------------------------------------------------------------------------------------------------------------------
city=input('Enter the full address or just city name:')
if 'bangalore' in city.lower():
    postal_code=int(input('Postal code is:'))
    if postal_code.is_integer() and postal_code==560000:
        print('We can reach you in time...')
else:
    print('Sorry! the product cannot be delivered to the address you are entering.')

#-----------------------------------------------------------------------------------------------------------------
def market():
    print("Welcome to ABC super market's inspection portal")
    today_date = input("Today's Date is:")
    Product_code = int(input('Enter the product code:'))
    if Product_code not in [1,2,3,4,5]:
        print("Enter the existing product code")
        exit()
    Product_name = input("Product name:")
    ds = int(today_date.split('/')[0])
    if ds - list[Product_code-1][2] < int(list[Product_code-1][3].split('/')[0]):
        print('Good to sale')
    else:
        print('Expired')
list=[(1,'Soap',12,'01/02/22'),(2,'shampoo',6,'03/14/22'),(3,'Toothpaste',7,'02/12/22'),(4,'Ready juice',2,'11/08/22'),(5,'chips',1,'11/20/22')]
market()


