from abc import ABC, abstractmethod



class ShoppingCart(ABC):

    @abstractmethod
    def display_products(self):
        pass

    @abstractmethod
    def add_to_cart(self, product_name, quantity):
        pass



class Cart(ShoppingCart):
    def __init__(self):
        self.products = {
            'Sugar': 50,
            'Rice': 55,
            'Wheat flour': 55,
            'Toor dal': 150,
            'Rava': 70
        }
        self.cart = []

    def display_products(self):
        print("Product: Price in Rs.")
        for product, price in self.products.items():
            print(f"{product}: {price}")

    def add_to_cart(self, product_name, quantity):
        if product_name not in self.products:
            print("Please enter the existing product's name in the list")
            return

        if quantity <= 0:
            print("Thank you")
            return

        price = self.products[product_name]
        total_price = price * quantity
        self.cart.append({'product': product_name, 'quantity': quantity, 'price': total_price})

        # Display the cart content
        print("\nCart:")
        print("Product: Quantity: Price in Rs.")
        for item in self.cart:
            print(f"{item['product']}: {item['quantity']}: {item['price']}")

        print("Thank you")

i=1
while i<10:

    def main():
        cart = Cart()
        cart.display_products()

        product_name = input("Enter the item name to add it to the cart: ")
        quantity = int(input("Enter the quantity in Kgs: "))

        cart.add_to_cart(product_name, quantity)


    if __name__ == "__main__":
        main()
    i+=1
