import time as t
items={'sugar':50,'rice':55,'wheat flour':55,'toor dal':150,'rava':70,'Sugar':50,'Rice':55,'Wheat flour':55,'Toor dal':150,'Rava':70}
print("WELCOME TO THE XYZ SHOP")
print("50% Off on Wheat Flour and 50% off on the sugar if you buy 2 Kg")
print("""items list:
      sugar:50
      rice:55
      wheat flour:55
      Toor dal:150
      rava:70""")
print("*********************************************************************")
def discount_wheat(price,kg):
    price=(price/2)*kg
    print("You got 50% discount")
    return price
def discount_sugar(price,kg):
    a=kg%2
    price=(a*price)+(kg-a)*(price/2)
    return price

def price(price,kg):
    price=price*kg
    return price
def shop(item,kg):
    if item in (items.keys() or l2):
        if item=='sugar'or item=='Sugar':
            a=discount_sugar(items[item],kg)
            print("You have to pay {} ruppes.".format(a))
            t.sleep(2)
        elif item=='wheat flour' or item=='Wheet flour':
            a=discount_wheat(items[item],kg)
            print("You have to pay {} ruppes.".format(a))
            t.sleep(2)
        elif item=='rice'or item=='Rice' or item=='Toor dal'or item=='toor dal'or item=='rava'or item=='Rava':
            p=price(items[item],kg)
            print("You have to pay {} ruppes.".format(p))
            t.sleep(2)
        else:
            print("Invalid Menu Option")
    else:
        print("Please Enter item from above list Only.")
l1=items.keys()
l2=[]
for i in l1:
    l2.append(i.capitalize())

while True:
     item=input("Enter item:")
     if item in items.keys() or l2:
         kg=int(input("How many kgs do you want?"))
         shop(item,kg)
     else:
         print("Please Enter item from above list")
     t.sleep(1)
