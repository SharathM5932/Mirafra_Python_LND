class Display:
    def __init__(self, a):
        self.a = a
        self.prod_cat = {
            'red tshirt': 'cloth',
            'trending_tshirt': 'cloth',
            'branded tshirt': 'cloth',
            'cotton tshirt': 'cloth',
            'dr.set': 'toy',
            'kitchen set': 'toy',
            'teddy': 'toy',
            'unicorn': 'toy',
            'fishing': 'toy',
            'chair': 'furniture',
            'table': 'furniture',
            'sofa': 'furniture'
        }

    def similar(self):
        if self.a in self.prod_cat:
            print(f"Item name: {self.a.capitalize()}")
        else:
            print("No matching item found.")
            return

        category = self.prod_cat[self.a]

        print("Suggested items for you:")
        suggestions=[]
        for item, cat in self.prod_cat.items():
            if cat==category and item != self.a:
                suggestions.append(item)
        if len(suggestions)>0:
            for i in suggestions:
                print(f" {i}")
        else:
            print("No similar items found.")

k = input("Search: ")
obj = Display(k)
obj.similar()
