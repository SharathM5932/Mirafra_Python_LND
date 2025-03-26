def filter1(saree):
    color, saree_type, price = saree[0], saree[1], saree[2]
    if 'red' in color and 'Silk' in saree_type and price <= 10000:
        return True
    return False


input_sarees = input("Enter the product details to store it into our data base:")
saree = eval(input_sarees)
a=[]
for code, details in saree.items():
    print(f"Checking product {code}: {details}")
    # Filtering based on conditions
    result = filter1(details)
    if result:
        a.append(code)
print(a)

#{'s1':['red','Silk',4500],'s2':['blood red','Silk',11500],'s3':['pink','Silk',11200],'s4':['rose red','Party wear',6999],'s5':['lemon yellow','Silk',8500],'s6':['brick red','Silk',8500], 's7':['Green','Party wear',8999],'s8':['brick red','cotton',1500],'s9':['Candy red','Silk',8500],'s10':['Ruby red','Silk',9999],}

'''input_sarees = input("Enter the product details to store it into our data base:")
saree=eval(input_sarees)
saree_list=list(filter(lambda n:'red' in saree[n][0] and saree[n][1]=='Silk' and saree[n][2]<= 10000,saree))
print(saree_list)'''

