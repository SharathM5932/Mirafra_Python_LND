from abc import ABC, abstractmethod
class Cart(ABC):
    @abstractmethod
    def display(self):pass
    @abstractmethod
    def _quantity(self):pass
class Execute(Cart):
    def display(self):
        return "Product:Price in Rs.\nSugar:50\nRice:55\nWheat flour:55\nToor dal:150\nRava:70"
    def _quantity(self):
        product = input("Enter the item name to add it to the cart:")
        pd = {'Sugar': 50, "Rice": 55, "Wheat flour": 55, "Toor dal": 150, "Rava": 70}
        if product in pd.keys():
            self.quantity = int(input("Enter the quantity in Kgs:"))
            if self.quantity > 1:
                print(f"Product: Quantity: Price in Rs.\n{product}:{self.quantity}:{pd[product] * self.quantity}")
            print("Thank you")
        else:
            print("Please enter the existing product's name in the list")

obj2=Execute()
print(obj2.display())
obj2._quantity()
