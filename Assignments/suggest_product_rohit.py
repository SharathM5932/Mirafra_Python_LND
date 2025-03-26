item=input("Search:")
cloth=['red tshirt','trending tshirt','branded tshirt','cotton tshirt']
toy=['Dr.set','kitchen set','teddy','unicorn','fishing']
furniture=['chair','table','sofa']
if item in cloth:
    print(f"Item name: {item}\nSuggested items for you:")
    cloth.remove(item)
    for i in cloth:print(i)
elif item in toy:
    print(f"Item name: {item}\nSuggested items for you:")
    toy.remove(item)
    for i in toy: print(i)
elif item in furniture:
    print(f"Item name: {item}\nSuggested items for you:")
    furniture.remove(item)
    for i in furniture: print(i)
else:
    print("No matching item found.")



