"""Eva furniture center
In Eve furniture center there are 4 floors. Basement is for car parking.
In ground floor, all small dismantled furniture, packed in cotton boxes are stored.
Furniture are stored in such a way that they can be searched easily.
Ex: For every product there will be a product code
which will be holding more details about product like: name, price, location in the ground floor to get the product and
quantity present in the furniture center.
If the customer likes a product which will be showcased in the 1st and 2nd floors, by seeing the label on the product,
they can get all the details.
And, if the product is small like chair or desk customer has to collect it by going to ground floor by him/her self.
The exact location i.e. in ground floor in which bay, row and column the customer can get the product,
will be mentioned on the product itself along with the product code.
For ex: B1R1C1 means: Bay 1, Row 1 and column 1.
But if the product is big enough which won’t be fitting in the customer’s car like a table or a sofa,
then they have to pay delivery charge of Rs.600/- and can expect it to arrive to their home itself.
Now being a developer create an app which can do this task automatically.
Store the data given as your database.
If the customer enters the product code along with the product price suitable details should be displayed.
Note: If the product code is wrong, display the appropriate message.
And, if the product quantity is zero then display the out of stock message.
Data:"""
def product_info(code):
    if code=="pdcc01":
        print("Product Type:",product_code[1]['Name'])
        print("Price:",product_code[1]['Price'])
        print("You can collect the product in the ground floor, Bay: 1 Row: 1 Column: 2 \n")
        product_code[1]['Quantity']-=1

    elif code=="pdcs11":
        print("Product Type: Sofa")
        print("Product Price: {} + {}/- Rs. Delivery charge.".format(product_code[2]['Price'],600))
        print("Please pay Rs. {}".format(product_code[2]['Price']+600))
        print("The product will be delivered to your home.\n")

    elif code=="pdct25":
        print("Product Type: Table")
        print("Product Price: {} + {}/- Rs. Delivery charge.".format(product_code[3]['Price'],600))
        print("Please pay Rs. {}".format(product_code[3]['Price']+600))
        print("The product will be delivered to your home.\n")

    elif code=="pdcd011":
        print("Product Type:",product_code[4]['Name'])
        print("Price:", product_code[4]['Price'])
        print("You can collect the product in the ground floor, Bay: 4 Row: 2 Column: 3\n")
        product_code[4]['Quantity']-=1

    elif code=="pdcR012":
        print("Product Type:",product_code[5]['Name'])
        print("Price:", product_code[5]['Price'])
        print("You can collect the product in the ground floor, Bay: 5 Row: 1 Column: 4\n")
        if product_code[5]['Quantity']==0:
            print("Sorry! Out of stock\n")
        else:
            pass
        product_code[5]['Quantity']-=1

    else:
        print("Please Enter the Valid Product Code\n")


product_code={1:{'code':"pdcc01",'Name':'Chair','Price':1500,'Location':'B1R1C2','Quantity':2},
              2:{'code':"pdcs11",'Name':'Sofa','Price':50000,'Location':'B2R4C1','Quantity':'Home'},
              3:{'code':"pdct25",'Name':'Table','Price':1500,'Location':'B3R3C2','Quantity':'Home'},
              4:{'code':"pdcd011",'Name':'Desk','Price':900,'Location':'B4R2C3','Quantity':13},
              5:{'code':"pdcR012",'Name':'Shelf','Price':2500,'Location':'B5R1C4','Quantity':0}
              }
i=1
while(i<1000):
    print("Sample Case {}".format(i))
    code=input("Please enter the product code:")
    i+=1
    if code=="pdcc01" or "pdcs11" or "pdct25" or "pdcd011" or "pdcR012":
        product_info(code)

    else:
        print("Please Enter the Valid Product Code")
        break





