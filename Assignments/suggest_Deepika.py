
products = {
    'tshirt': ['red tshirt', 'trending tshirt', 'branded tshirt', 'cotton tshirt',],
    'chair': ['chair', 'sofa', 'table'],
    'teddy':['Dr.set','Kitchen set','unicorn','teddy','fishing']


}


def suggest_products(search_term):

    found = False
    for category, items in products.items():
        if search_term.lower() in [item.lower() for item in items]:
            found = True
            print(f"Item name: {search_term}")
            print("Suggested items for you:")
            for item in items:
                if item.lower() != search_term.lower():
                    print(item)
            break

    if not found:
        print("No matching item found.")

i=1
while i<10:
    print("Sample case {}".format(i))
    search_query = input("Search: ").strip()
    suggest_products(search_query)
    i+=1








