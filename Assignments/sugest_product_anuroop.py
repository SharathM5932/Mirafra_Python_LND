# without class
# dict1={'red tshirt':['trending tshirt','branded tshirt','cotton tshirt'],
#        'chair':['table','sofa']}
# product_name=input("Search:")
# if product_name in dict1:
#     print("Item name:",product_name)
#     print("Suggested items for you:")
#     for item in dict1[product_name]:
#         print(item)
# else:
#     print("No matching item found.")

# using class
class product:
    def __init__(self):
        self.dict1={'red tshirt':['trending tshirt','branded tshirt','cotton tshirt'],
        'chair':['table','sofa']}

    def inputs(self):
        product_name = input("Search:")
        if product_name in self.dict1:
            print("Item name:", product_name)
            print("Suggested items for you:")
            for item in self.dict1[product_name]:
                print(item)
        else:
            print("No matching item found.")


p1=product()
p1.inputs()





