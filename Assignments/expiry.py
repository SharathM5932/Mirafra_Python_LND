data = {1: ['Soap',12, '01/02/22'],2:['Shampoo',6,'03/14/22'],3:['Toothpaste',7,'02/12/22'],
        4:['Ready juice',2,'11/08/22'],5:['Chips',1,'11/20/22']}
print("Welcome to ABC  super market's inspection portal")
date ='12/1/22'
td=list(map(lambda x:int(x),date.split('/')))
print('Enter the product code:')
product_code=int(input())
if product_code in list(data.keys()):
    print('product name is:',data[product_code][0])
    bb=data[product_code][1] #12
    m_d=data[product_code][2] #['01', '02', '22']
    md=list(map(lambda x:int(x),m_d.split('/')))
    ed = []
    m = md[0] + bb

    if m > 12:
        um = m - 12
        y = md[2] + 1
        d = md[0]
    else:
        um = m
        y = md[2]
        d = md[0]
    ed = [um, d, y]
    #print(ed)
    #print(td)
    if ed[2] > td[2]:
        print('Good to sale')
    elif ed[2]==td[2]:
        if ed[0] > td[0]:
            print('good to sale')
        elif ed[0] == td[0]:
            if ed[1] >= td[1]:
                print('good to sale')
            else:
                print('expired already')
        else:
            print('expired already')
    else:
        print('expired already')
else:print('product code not found')
