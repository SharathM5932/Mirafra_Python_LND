data={'Sugar':50,'Rice':55,'Wheat flour':55,'Toor dal':150,'Rava':70}
print('Welcome to our shop.The list items:')
print('Product:Price in Rs.')
for i in data:
    print(f'{i}:{data[i]}')
print('''For your surprise we have offers going on:
Buy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour.''')
print('Enter the item name: ')
item=input()
print("Enter the quantity in KG's ")
quantity=int(input())
if item=='Sugar' or item=='Wheat flour':
    if item=='Sugar':
        if quantity>=2:
            print(f"You have asked for  {quantity} KG {item} Please pay Rs.:",(quantity*data[item])/2)
        else:
            print(f"You have asked for  {quantity} KG {item} Please pay Rs.:",(quantity*data[item]))
            exit
    else:
        print(f"You have asked for  {quantity} KG {item} Please pay Rs.:", (quantity * data[item]) / 2)

else:
    print(f"You have asked for  {quantity} KG {item} Please pay Rs.:", (quantity * data[item]))
