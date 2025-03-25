products = {'pdcR012': {'type': 'Shelf','price': None,'location': None,'quantity': 0,},
'pdcc01': {'type': 'Chair','price': 1500,'location': 'Bay 1 Row 1 Column 2','quantity': 5,},
'pdcs11': {'type': 'Sofa','price': 50000,'location': None,'quantity': 2,},}

def search_product(product_code):
    if product_code in products:
        y=products[product_code]
        if y['quantity']==0:
            print(f"Product Type: {y['type']}\nSorry! Out of stock")
        elif y['location']:
            print(f"Product Type: {y['type']}\n"
                    f"Price: {y['price']}\n"
                    f"You can collect the product in the ground floor, {y['location']}")
        else:
            print(f"Product Type: {y['type']}\n"
                    f"Product Price: {y['price']} + 600/- Rs. Delivery charge.\n"
                    f"Please pay Rs. {y['price'] + 600}\n"
                    "The product will be delivered to your home.")
    else:
        print("Please enter a valid product code.")
i=1
while i<10:
    print("Sample case {}:".format(i))
    product_code=input("Please enter the product code: ")
    result = search_product(product_code)
    print(result)
    i+=1
