l=[['trending tshirt','branded tshirt','cotton tshirt','red tshirt'],
['Dr.set','kitchen setred', 'teddy','unicorn','fishing'],
['chair','table','sofa']]

product=input("Search:")
for i in l:
    if product in i:
        print(f'Item name:{product}')
        print("Suggested items for you:")
        for j in i:
            if j==product:pass
            else:print(j)
        break

else:
    print("No matching item found.")



