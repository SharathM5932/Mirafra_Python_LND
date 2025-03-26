data={'pdcc01':["Chair",1500,'B1R1C2',2],
      'pdcs11':['Sofa',50000,'B2R4C1','Home'],
      'pdct25':['Table',15000,'B3R3C2','Home'],
      'pdcd011':['Desk',900,'B4R2C3',13],
      'pdcR012':['Shelf',2500,'B5R1C4',0]}
code=input('Please enter the product code:')
if code in data.keys():
    l = data[code][2]
    print(f'Product Type:{data[code][0]}')
    if data[code][3]=="Home" or data[code][3]>0:
        if data[code][3]=='Home':
            print(f'Product Price: {data[code][1]} + 600/- Rs. Delivery charge.')
            print('Please pay Rs.', data[code][1] +600)
            print('The product will be delivered to your home.')
        else:
            print(f'Price:{data[code][1]}')
            print(f'You can collect the product in the ground floor, Bay: {l[1]} Row: {l[3]} Column: {l[5]}')
    else:print('Sorry! Out of stock')
else:print('Please enter a valid product code.')
