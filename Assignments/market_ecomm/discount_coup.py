# discount.py


coupon_code = ['CDEC01', 'ONEJAN02', '2234150', 'WHEAT50', 'SUGAR2KG']


def check_coupon(cart):
    print("Checking for discounts...")
    cart_value = sum(items[item] * quantity for item, quantity in cart.items())
    print(f"Cart value: ₹{cart_value}")

    n = input("Do you have a coupon? Type Y or N: ").upper()
    if n == 'Y':
        coupon = input("Enter the coupon code: ").upper()
        if coupon == 'WHEAT50':
            if 'Wheat flour' in cart:
                cart['Wheat flour'] *= 0.5
                print("50% off on Wheat applied.")
            else:
                print("Wheat flour is not in the cart.")
        elif coupon == 'SUGAR2KG':
            if 'Sugar' in cart and cart['Sugar'] >= 2:
                sugar_qty = cart['Sugar']
                cart['Sugar'] = (sugar_qty // 2 + sugar_qty % 2)
                print("50% off on 2kg of Sugar applied.")
            else:
                print("Not enough Sugar in the cart for this discount.")
        elif coupon in coupon_code:
            # Handle other coupons
            print("Other discounts applied.")
        else:
            print("Invalid coupon code.")

    total_cost = sum(items[item] * quantity for item, quantity in cart.items())
    print(f"Total cost after discount: ₹{total_cost}")
    return total_cost
