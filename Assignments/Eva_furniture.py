products = {
    "pdcc01": {
        "name": "Chair",
        "price": 1500,
        "location": "B1R1C2",
        "quantity": 2,
        "size": "small"
    },
    "pdcs11": {
        "name": "Sofa",
        "price": 50000,
        "location": "Home",
        "quantity": 1,
        "size": "large"
    },
    "pdct25": {
        "name": "Table",
        "price": 15000,
        "location": "Home",
        "quantity": 1,
        "size": "large"
    },
    "pdcd011": {
        "name": "Desk",
        "price": 900,
        "location": "B4R2C3",
        "quantity": 13,
        "size": "small"
    },
    "pdcR012": {
        "name": "Shelf",
        "price": 2500,
        "location": "B5R1C4",
        "quantity": 0,
        "size": "small"
    }
}
def search_prod(product_code):
    if product_code in products:
        product=products[product_code]
        if product['quantity']==0:
            print(f"Product Type: {product['name']}")
            print("Sorry! Out of stock")
        else:
            product_price=product['price']
            if product['size']=='large':
                print(f"Product Type: {product['name']}")
                print(f"Product Price: {product['price']} + 600/- Rs. Delivery charge.")
                total_price = product["price"] + 600
                print(f"Please pay Rs. {total_price}")
                print(f"The product will be delivered to your home.")
            elif product['size']=='small':
                print(f"Product Type: {product['name']}")
                print(f"Price: {product['price']}")
                print(f"You can collect the product in the ground floor, Bay: {product['location'][1]} Row: {product['location'][3]} Column: {product['location'][5]}")
    else:
        print("Please enter a valid product code.")


product_code=input("Please enter the product code: ")
search_prod(product_code)






