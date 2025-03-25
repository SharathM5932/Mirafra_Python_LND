#suggest products
all=['red tshirt','trending tshirt','branded tshirt','cotton tshirt','Dr.set','Kitchen set','teddy','unicorn','fishing','chair','table','sofa']
products={'cloth':['red tshirt','trending tshirt','branded tshirt','cotton tshirt'],
          'toy':['Dr.set','Kitchen set','teddy','unicorn','fishing'],
          'furniture':['chair','table','sofa']}
def suggest_products(search):
        if search in products['cloth']:
            for x in products['cloth']:
                if x==search:
                    continue
                print(x)
            print()
        elif search in products['toy']:
            for x in products['toy']:
                if x==search:
                    continue
                print(x)
            print()
        elif search in products['furniture']:
            for x in products['furniture']:
                if x==search:
                    continue
                print(x)
            print()

i=1
while i<1000:
    print("Sample Case {}".format(i))
    search=str(input("Search:"))
    if search in all:
        print("Item Name: {}".format(search))
        print("Suggested items for you:")
        suggest_products(search)
    else:
        print("No matching item found.")
    i+=1
