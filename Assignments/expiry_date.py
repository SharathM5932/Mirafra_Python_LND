from datetime import datetime
formatted_date = datetime.now().strftime('%m/%d/%y')
date_compare = datetime.strptime(formatted_date, '%m/%d/%y')

products = {
    'P1': {'name': 'Soap', 'expiry_date': '12/10/21'},
    'P2': {'name': 'Milk', 'expiry_date': '01/12/25'},
    'P3': {'name': 'Shampoo', 'expiry_date': '11/30/23'},
    'P4': {'name': 'Toothpaste', 'expiry_date': '02/05/25'},
    'P5': {'name': 'Bread', 'expiry_date': '12/05/25'},
    'P6': {'name': 'Juice', 'expiry_date': '01/20/22'},
    'P7': {'name': 'Cheese', 'expiry_date': '12/25/24'},
    'P8': {'name': 'Butter', 'expiry_date': '01/10/25'},
    'P9': {'name': 'Yogurt', 'expiry_date': '01/18/25'},
    'P10': {'name': 'Cereal', 'expiry_date': '12/31/24'},
}
print("Welcome to ABC  super market's inspection portal ".center(80,'='),end="\n")
print(f"Today's date is: {date_compare}")
while True:
    id=input("Enter product id: ").upper()
    if id in products:
        print(f"Product Name: {products[id]['name']}")
        expirydate = datetime.strptime(products[id]['expiry_date'], '%m/%d/%y')
        if expirydate < date_compare:
            print(f"Expired on {products[id]['expiry_date']}")
        else:
            print(f"Good to Sale")
    elif id=='DONE':
        break
    else:
        print("Enter the existing product code.")
        break

