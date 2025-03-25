# scenario1
'''import re
address=input("Enter the full address or just city name:")
dict1={"bengaluru":560000,
       "mumbai":560001}
for key,val in dict1.items():
    if re.search(key,address):
        print("Postal code is:",dict1[key])
        print("We can reach you in time...")
        break
    elif re.search(str(val),address):
        print("Postal code is:",dict1[key])
        print("We can reach you in time...")
        break
    else:
        print("Sorry! the product cannot be delivered to the address you are entering.")'''

# scenario2
'''from datetime import datetime
def validate_date(n,dict2):
    date1 = datetime(2025, 2, 14)
    print(int(dict2[n][1][6:]), int(dict2[n][1][3:5]), int(dict2[n][1][:2]))
    date2 = datetime(int(dict2[n][1][6:]), int(dict2[n][1][3:5]), int(dict2[n][1][:2]))
    difference = (date1 - date2).days
    print(difference)
    if difference <= 30:
        print("Good to sale")
    else:
        print("Expired")

n=int(input("code:"))
dict2={1:['soap','13/01/2025'],
       2:['shampoo','01/12/2024']}
if n in dict2:
    print("prod:",dict2[n][0])
    validate_date(n,dict2)
else:
    print("Enter the existing product code.")'''

# --scenario3-------------------
# def find_price(item_name,quantity,dict1):
#     total=0
#     if dict1[item_name][1]==True:
#         while quantity>0:
#             total+=dict1[item_name][0]
#             quantity=quantity%2
#         return total
#     else:
#         total=1
#         total=quantity*dict1[item_name][0]
#         return total
#
#
# t=int(input("t:"))
# prices='''Welcome to our shop.The list items:
# Product:Price in Rs.
# Rava:70
# Rice:55
# Sugar:50
# Toor dal:150
# Wheat flour:55
# For your surprise we have offers going on:
# Buy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour.'''
# print(prices)
# item_name=input("Enter the item name:")
# dict1={'rava':[70,False],
# 'rice':[55,False],
# 'sugar':[50,True],
# 'toor dal':[150,False],
# 'wheat flour':[55,True]}
# n_item_name=item_name.lower()
# if n_item_name in dict1:
#     try:
#         quantity = int(input("Enter the quantity in KGs:"))
#         print(f"You have asked for  {quantity} KG {item_name}")
#         print("Please pay Rs.:", find_price(n_item_name, quantity,dict1))
#     except ValueError:
#         print("Please enter input in integer.")
# else:
#     print("Enter the item name not present in our shop and try again.")



