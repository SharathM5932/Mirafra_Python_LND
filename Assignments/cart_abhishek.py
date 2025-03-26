from abc import ABC,abstractmethod
class ac(ABC):
    @abstractmethod
    def display(self):
        pass
class item(ac):
    def __init__(self,data):
        self.data=data
    def display(self):
        print("Product:Price in Rs.")
        for i in  self.data:
            print(f"{i}:{self.data[i]}")
class cal(ac):
    def __init__(self,choice,quantity,data):
        self.data=data
        self.choice=choice
        self.quantity=quantity
    def display(self):
        print("Cart:")
        print("Product: Quantity: Price in Rs.")
        print(f"{self.choice}: {self.quantity}: {self.data[self.choice]*self.quantity}")
        print("Thank you")
d={
    'Sugar':50,'Rice':55,'Wheat flour':55,'Toor dal':150,'Rava':70
}
obj=item(d)
obj.display()
choice=input("Enter the item name to add it to the cart:")
if choice in d.keys():
    quantity=(int(input("Enter the quantity in Kgs:")))
    obj2=cal(choice,quantity,d)
    obj2.display()
else:print("Please enter the existing product's name in the list")
