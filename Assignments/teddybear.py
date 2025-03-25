

def find_teddy_bears(products_string):

    products = products_string.split(", ")
    teddy=[product for product in products if 'teddy' in product.lower()]
    print("Enter the name of products stored in the cotton box:{}".format(input))
    print("Dear Surya,")
    print(f"Total {len(teddy)} teddies are there. And, here they are:")
    print(teddy)

input ="stuffed toy teddy, special one, toy teddy, love toy, teddy bear, pink teddy, red teddy, Mr. teddy, my bear, love bear, deer, gift me"
find_teddy_bears(input)





