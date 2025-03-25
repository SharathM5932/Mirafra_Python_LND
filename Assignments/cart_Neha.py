from abc import ABC, abstractmethod
class Cart(ABC):
    def __init__(self,item_p,quant):
        self.item_p=item_p
        self.quant=quant
    @abstractmethod
    def prize(self,item_p,quant):
        pass
class Cart_prize(Cart):
    def __init__(self,item_p,quant):
        Cart.__init__(self,item_p,quant)
    def prize(self,item_p,quant):
        prize=(item_p*quant)
        print(prize)
        return prize

data={'Sugar':50,'Rice':50,'Wheat flour':55,'Toor dal':150,'Rava':70}
i=1
while i<100:
    print("Sample Case {}".format(i))
    print("""Product:Price in Rs.
Sugar:50
Rice:55
Wheat flour:55
Toor dal:150
Rava:70""")
    item=input("Enter the item name to add it to the cart:")
    if item in data:
        quantity = int(input("Enter the quantity in Kgs:"))
        if quantity>0:
            item_prize=int(data[item])
            print(item_prize)
            obj_Cart=Cart_prize(item_prize,quantity)
            price=obj_Cart.prize(item_prize,quantity)
            print("Cart:")
            print("Product: Quantity: Price in Rs.\n{}: {}:{} ".format(item,quantity,price))
        elif quantity==0:
            pass
        print("Thank You")
        print()
    else:
        print("Please enter the existing product's name in the list")
    print()
    i+=1