from abc import ABC,abstractmethod
class Product(ABC):
    @abstractmethod
    def calculate_amount(self,name):
        pass
class customer(Product):
    def __init__(self,product_price,quantity):
        self.product=product_price
        self.quantity=quantity
    def calculate_amount(self):
        return self.product*self.quantity


dict1={'sugar':[50,2],
       'rice':[55,2],
       'wheat flour':[55,2],
       'toor dal':[150,2],
       'rava':[70,1]}
str1 = '''Product:Price in Rs.
        Sugar:50
        Rice:55
        Wheat flour:55
        Toor dal:150
        Rava:70'''
print(str1)
product = input("Enter the item name to add it to the cart:").lower()
if product in dict1:
    quantity = int(input("Enter the item name to add it to the cart:"))
    if quantity > 0 and dict1[product][1] > 0:
        # c1=customer(product,quantity)
        c1 = customer(dict1[product][0], quantity)
        price=c1.calculate_amount()
        print("Cart:")
        print("Product: Quantity: Price in Rs.")
        print(product, ":", quantity, ":", price)
        print("Thank you")
    else:
        print("Thank you")
else:
    print("Please enter the existing product's name in the list")