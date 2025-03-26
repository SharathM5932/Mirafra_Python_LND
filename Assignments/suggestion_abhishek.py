d={"cloth":['trending tshirt','branded tshirt','cotton tshirt','red tshirt'],
 "toy":['Dr.set','kitchen setred', 'teddy','unicorn','fishing'],
 "furniture":['chair','table','sofa']}
product=input("Search:")
for i in d.values():
    if product in i:
        print(f'Item name:{product}')
        print("Suggested items for you:")
        for j in i:
            if j==product:pass
            else:print(j)
        break
else:
    print("No matching item found.")