# market.py

items = {
    'Wheat flour': 40,
    'Sugar': 30,
    'Rice': 50,
    'Milk': 25,
    'Eggs': 5,
    'Butter': 100,
    'Cheese': 80,
    'Oil': 120,
    
}

def cal_price(item, quantity):
    price_per_unit = items[item]
    return price_per_unit * quantity

def shopping_cart():
    print("Welcome to getNgo market".center(50, '-'))
    print("Select your items to order".center(50, '-'))
    for index, (keys, values) in enumerate(items.items(), start=1):
        print(f"{index}) {keys}: ₹{values}\n")
    print("Go to Cart press 9\n")

    cart = {}
    while True:
        k = int(input('Press your item number to order \n (Press 9 to Checkout): '.center(20, '-')))
        item_keys = list(items.keys())
        if 1 <= k <= len(item_keys):
            selected_item = item_keys[k - 1]
            quantity = int(input(f"Enter KGs: {selected_item} "))
            cart[selected_item] = cart.get(selected_item, 0) + quantity
        elif k == 9:
            break
        else:
            print("Invalid selection!")

    return cart
