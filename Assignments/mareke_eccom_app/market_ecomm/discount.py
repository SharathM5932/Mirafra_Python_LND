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
coupon_code = ['CDEC01', 'ONEJAN02', '2234150', 'WHEAT50', 'SUGAR2KG']

def check_coupon(cart, coupon):
    print("Checking for discounts...")
    if coupon == 'WHEAT50':
        if 'Wheat flour' in cart:
            cart['Wheat flour'] *= 0.5
            print("50% off on Wheat applied.")
    elif coupon == 'SUGAR2KG':
        if 'Sugar' in cart and cart['Sugar'] >= 2:
            cart['Sugar'] = cart['Sugar'] // 2 + cart['Sugar'] % 2
            print("50% off on 2kg of Sugar applied.")
    elif coupon in coupon_code:
        print("Other discounts applied.")
    else:
        print("Invalid coupon code.")

    return sum(items[item] * quantity for item, quantity in cart.items())
