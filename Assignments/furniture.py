# product_details={
#     'pdcR012':{'Product Type':'Shelf','Price':2500,'location':'B5R1C4','quantity':0},
#     'pdcc01':{'Product Type':'Chair','Price':1500,'location':'B1R1C2','quantity':2},
#     'pdcs11':{'Product Type':'Sofa','Price':50000,'location':'B2R4C1','quantity':'Home'},
#     'pdct25':{'Product Type':'Table','Price':15000,'location':'B3R3C2','quantity':'Home'},
#     'pdcd011':{'Product Type':'Desk','Price':900,'location':'B4R2C3','quantity':14}
# }
# # product_code=input('Sample case 1:\nPlease enter the product code:')
# # for i,j in d.items():
# #     for i1,j1 in j.items():
# #         if i1 == product_code and 'quantity'==0:
# #             print('Sorry! Out of stock')
# def sample(product_code):
#     if product_code not in product_details:
#         return "Please enter a valid product code."
#     product=product_details[product_code]
#     if product['quantity']==0:
#         return f"Product Type: {product['Product Type']}\nSorry! Out of stock"
#     details = f"Product Type: {product['Product Type']}\n"
#     details += f"Price: {product['Price']}\n"
#     if product['location']:
#         details += f"You can collect the product in the ground floor, Bay: {product['location'][0]} Row: {product['location'][1]} Column: {product['location'][2]}"
#     else:
#         if product["Product Type"] == "Sofa" or product["Product Type"] == "Table":
#             delivery_charge = 600
#             total_price = product["Price"] + delivery_charge
#             details += f"Product Price: {product['Price']} + {delivery_charge}/- Rs. Delivery charge.\n"
#             details += f"Please pay Rs. {total_price}\n"
#             details += "The product will be delivered to your home."
#
#     return details
# def main():
#     product_code = input("Please enter the product code: ")

def main():

    products = {
        "pdcR012": {"type": "Shelf", "price": 0, "quantity": 0, "location": None},
        "pdcc01": {"type": "Chair", "price": 1500, "quantity": 10, "location": "B1R1C2"},
        "pdcs11": {"type": "Sofa", "price": 50000, "quantity": 5, "location": None},
        "pdct01": {"type": "Table", "price": 20000, "quantity": 3, "location": None}
    }


    product_code = input("Please enter the product code: ").strip()
    if product_code not in products:
        print("Please enter a valid product code.")
        return

    product = products[product_code]
    if product["quantity"] == 0:
        print(f"Product Type: {product['type']}")
        print("Sorry! Out of stock")
        return
    print(f"Product Type: {product['type']}")

    if product["type"] == "Sofa" or product["type"] == "Table":
        total_price = product["price"] + 600
        print(f"Product Price: {product['price']} + 600/- Rs. Delivery charge.")
        print(f"Please pay Rs. {total_price}")
        print("The product will be delivered to your home.")
    else:
        print(f"Price: {product['price']}")
        print(f"You can collect the product in the ground floor, Bay: {product['location'][1]} Row: {product['location'][3]} Column: {product['location'][5]}")
main()