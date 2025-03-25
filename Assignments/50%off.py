import time as t
x={'Rava':70,'rava':70,'Rice':55,'rice':55,'Sugar':50,'sugar':50,'Toor dal':150,'toor dal':150,
'Wheat Flour':55,'wheat flour':55}
print("Welcome to XYZ shop")
print("For your surprise we have offers going on:")
print("Buy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour.")
print("""list of items:
Rava:70
Rice:55
Sugar:50
Toor dal:150 
Wheat flour:55""")
print("****************************************")
def no_discount(price,g):
    price=price*g
    return price



def discount_sugar(price,kg):
    a=kg%2
    price=(a*price)+(kg-a)*(price/2)
    return price



def discount_wheat(price,kg):
    price=kg*(price/2)
    return price




def match(item,k):
    if item in x.keys():
        if item=='sugar':
            a=discount_sugar(x[item],k)
            print("You have to pay {}".format(a))
            t.sleep(2)
        elif item=='wheat flour':
            b=discount_wheat(x[item],k)
            print("You have to pay {}".format(b))
            t.sleep(2)
        elif item =='rice'or 'Rice' or 'Toor dal' or 'toor dal' or 'Rava' or 'rava':
            f=no_discount(x[item],k)
            print("You have to pay {}".format(f))
            t.sleep(2)
        else:
            print("No item")
    else:
        print("Idiot ,type from above list only.")
while True:
    item = input("enter the item: ")
    if item in x.keys():
        kg = int(input("how many kg you want: "))
        match(item, kg)
    else:
        print("Idiot ,type correctly")




