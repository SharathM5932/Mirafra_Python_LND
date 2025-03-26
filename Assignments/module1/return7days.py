from datetime import date,datetime,timedelta
database = [
    {"customer_name": "Narendra", "product_name": "Toy1", "price": 499},
    {"customer_name": "Sujata", "product_name": "Pink saree", "price": 7500},
    {"customer_name": "Shritan", "product_name": "T-shirt", "price": 500}
]
def return_prod(name,prod_name,date_prod):
    today = date.today()
    date_obj = datetime.strptime(date_prod, "%m/%d/%y").date()
    flag = False
    for customer in database:
        if name == customer['customer_name'] and prod_name == customer['product_name']:
            flag = True
            if today - date_obj <= timedelta(days = 7):
                print(f"Product:{customer['product_name']} will be collected from the delivered address and amount:{customer['price']} will be returned to your account.")
            else:
                print("Sorry! the product cannot be returned")
        break
    if not flag:
        print("You have not purchased that product recently with us.")


