from abc import ABC, abstractmethod


class Cart(ABC):
    @abstractmethod
    def display_items(self):
        pass

    @abstractmethod
    def add_to_cart(self, product_name, quantity):
        pass


class ShoppingCart(Cart):
    def __init__(self):
        self.products = {
            "Sugar": 50,
            "Rice": 55,
            "Wheat flour": 55,
            "Toor dal": 150,
            "Rava": 70
        }
        self.cart = {}

    def display_items(self):
        print("Product:Price in Rs.")
        for product, price in self.products.items():
            print(f"{product} : {price}")

    def add_to_cart(self, product_name, quantity):
        if product_name in self.products:
            if quantity > 0:
                self.cart[product_name] = {
                    "quantity": quantity,
                    "price_per_kg": self.products[product_name]
                }
                print("\nProduct: Quantity: Price in Rs.")
                for product, details in self.cart.items():
                    total_price = details["quantity"] * details["price_per_kg"]
                    print(f"{product}: {details['quantity']} KG, Rs. {total_price}")

            print("Thank you")
        else:
            print("Please enter the existing product's name in the list")

    '''def display_cart(self):
        print("\nProduct: Quantity: Price in Rs.")
        for product, details in self.cart.items():
            total_price = details["quantity"] * details["price_per_kg"]
            print(f"{product}: {details['quantity']} KG, Rs. {total_price}")
'''


shopping_cart = ShoppingCart()
shopping_cart.display_items()

product_name = input("\nEnter the item name to add it to the cart: ").capitalize()
quantity = float(input(f"Enter the quantity (in KG) of {product_name}: "))

shopping_cart.add_to_cart(product_name, quantity)


