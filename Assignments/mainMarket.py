# main.py

from market_ecomm.customer_signin import login
from market_ecomm.discount_coup import check_coupon
from market_ecomm.market import shopping_cart
# from market_ecomm.discount_coup import check_coupon
#
login()
cart = shopping_cart()
check_coupon(cart)

