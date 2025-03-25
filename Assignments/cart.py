cart={'Sugar':50,'Rice':55,'Wheat flour':55,
      'Toor dal':150,'Rava':70}
def items(x):
    if x in cart:
        y=int(input("Enter the quantity in Kgs:"))
        if y>0:
            a=cart[x]*y
            print("Cart: ")
            print("Product: Quantity: Price in Rs.\n {}: {}: {}".format(x,y,a))

            print("Thank you")
        else:
            print("Thank you")
    else:
        print("Please enter the existing product's name in the list")




i=1
while i<10:
    print("Sample case:{}".format(i))
    print("""'Sugar':50,
'Rice':55,
'Wheat flour':55,
'Toor dal':150,
'Rava':70""")
    x=input("Enter the item name to add it to the cart: ")

    items(x)
    i+=1
