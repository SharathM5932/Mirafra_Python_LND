# Capitalize names starting with the letter 'A' from the list 
# ['Alice', 'Bob', 'Anna', 'Tom'].
# Output:['ALICE', 'ANNA']

# words = ['Alice', 'Bob', 'Anna', 'Tom']
# up = list(map(lambda x: x.upper(), filter(lambda x: x[0] == 'A', words)))
# print(up)
#-----------------------------------------------------------------------------------------
# Find the square root of all positive numbers in 
# [-4, 9, 16, -1, 25].
# Output:[3.0, 4.0, 5.0]

# import math
# l1 = [-4, 9, 16, -1, 25]
# s = list(map(lambda x:math.sqrt(x), filter(lambda x: x > 0,l1)))
# print(s)
#-----------------------------------------------------------------------------------------
# Filter words containing the letter 'e' and convert them to uppercase. 
# Words: ['apple', 'orange', 'pear', 'banana'].
# Output:['APPLE', 'ORANGE', 'PEAR']

# l1 = ['apple', 'orange', 'pear', 'banana']
# s = list(map(lambda x:x.upper(), filter(lambda x: 'e' in x , l1)))
# print(s)
#-----------------------------------------------------------------------------------------
# From the list of tuples [(1, 5), (3, 6), (4, 4), (2, 9)], 
# filter tuples where the second element is greater than the first and compute their product.
# Output:[5, 18, 18]

# lis = [(1, 5), (3, 6), (4, 4), (2, 9)]
# s = list(map(lambda x: x[0]*x[1],(filter(lambda x: x[1] > x[0],lis))))
# print(s)

#-----------------------------------------------------------------------------------------
# Remove duplicate numbers from [2, 3, 2, 4, 5, 4] and calculate their squares.
# Output: [4, 9, 16, 25]

# l1 = [2, 3, 2, 4, 5, 4]
# s = set(map(lambda x: x**2, l1))
# print(list(s))
#-----------------------------------------------------------------------------------------
# Filter numbers divisible by 4 in the range 0-20 and divide them by 2.
# Output:[0.0, 2.0, 4.0, 6.0, 8.0, 10.0]


# s = list(map(lambda x: x/2, filter(lambda x: x%4==0,range(21))))
# print(s)
#-----------------------------------------------------------------------------------------
# For odd numbers in 0-9, calculate the sum of their squared digits.
# Output:[1, 9, 25, 49, 81]


# s = list(map(lambda x: x*x, filter(lambda x: x%2!=0, range(10))))
# print(s)

#-----------------------------------------------------------------------------------------
# Find all numbers in the range 1-50 that are divisible by both 3 and 5.
# Output: [15, 30, 45]


# s = list(filter(lambda x: x%3==0 and x%5==0,range(1,51)))
# print(s)

#-----------------------------------------------------------------------------------------
# Filter out vowels from the list 
# ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z'].
# Output:['a', 'e', 'i', 'o', 'u']


# words = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
# s = list(filter(lambda x: x in "aeiou",words))
# print(s)

#-----------------------------------------------------------------------------------------

# Find the lengths of words longer than 4 characters in the list 
# ['apple', 'is', 'tasty', 'cherry', 'banana'].
# words = ['apple', 'is', 'tasty', 'cherry', 'banana']
# output: [5, 5, 6]


# words = ['apple', 'is', 'tasty', 'cherry', 'banana']
# s = list(map(lambda x: len(x), filter(lambda x: len(x) > 4,words)))
# print(s)


#-----------------------------------------------------------------------------------------

# Filter palindromes from the list ['madam', 'hello', 'radar', 'world', 'level'].
# Output:['madam', 'radar', 'level']


# words = ['madam', 'hello', 'radar', 'world', 'level']
# s = list(filter(lambda x: x[::-1] ==x,words))
# print(s)


#-----------------------------------------------------------------------------------------

# Calculate the base-10 logarithm of numbers greater than 0 in 
# [1, 10, 100, 0, 1000].
# Output:[0.0, 1.0, 2.0, 3.0]

# import math
# lis = [1, 10, 100, 0, 1000]
# def fun(i):
#     if i > 0:
#         return math.log(i,10)

# s = list(map(fun,lis))
# print(s)

#-----------------------------------------------------------------------------------------

# Filter prime numbers in the range 0-49.
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# def prime(x):
#     if x <= 1:
#         return None
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return None
#     return x
    
# s = list(map(prime,range(50)))
# l = [i for i in s if i != None]
# print(l)


# l1=[4,5,6,7]
# l2=[2,3,5,6,7,9,2]
# s = l2[4:7]
# l = [x for x in zip(l1,l2) for x in x]

# l3 = [l[i] + l[i+1] for i in range(0,len(l)-1,2)]
# l3 += s
# for i in range(len(l3)-1):
#     if l3[i] > 10:
#         l3[i] = l3[i]-10
#         l3[i+1] = l3[i+1] + 1
# print(l3)

#fibnoccai series using generator
# def fib():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a+b
    
# f = fib()
# for i in range(6):
#     print(next(f))

#2. Write a generator that calculates the running sum of numbers sent to it using send. 
#If None is sent, it should return the current total.
# def gen():
#     total = 0
#     while True:
#         value = yield
#         if value is not None:
#             total += value
#         if value is None:
#             yield total
# g = gen()
# g.send(None)
# g.send(5)
# g.send(2)
# g.send(8)
# print(g.send(None))



#50%-off

# def menu():
#     print("Welcome to our shop.The list items: ")
#     print("Product:Price in Rs.")
#     print("Rava:70")
#     print("Rice:55")
#     print("Sugar:50")
#     print("Toor dal:150")
#     print("Wheat flour:55")
#     print("For your surprise we have offers going on: ")
#     print("Buy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour. ")

# def main():
#     menu()
#     item = input("Enter the item name: ")
#     quantity = int(input("Enter the quantity in KGs:"))
#     if item == 'Wheat flour':
#         price = (quantity*55)//2
#         print(f"You have asked for  {quantity} KG {item} ")
#         print(f"Please pay Rs.: {price}")
#     elif item == "Sugar":
#         dis_per_2kgs = 50 * 2 * 0.5
#         total_2kg_Sets = quantity//2
#         remainig_1kg = quantity %2
#         total_price = (total_2kg_Sets * dis_per_2kgs) + (remainig_1kg * 50)
#         print(f"You have asked for  {quantity} KG {item} ")
#         print(f"Please pay Rs.: {total_price}")
    
#     elif item == "Rava":
#         price = quantity * 70
#         print(f"You have asked for  {quantity} KG {item} ")
#         print(f"Please pay Rs.: {price}")

#     elif item == "Rice":
#         price = quantity * 55
#         print(f"You have asked for  {quantity} KG {item} ")
#         print(f"Please pay Rs.: {price}")
#     elif item =="Toor dal":
#         price = quantity * 150
#         print(f"You have asked for  {quantity} KG {item} ")
#         print(f"Please pay Rs.: {price}")
#     else:
#         print("Enter valid input") 


# main()

#Check the expired date

# def fun(manf_date,best_before_months):
#     todays_year = 22
#     todays_month = 12
#     todays_day = 1

#     manf_month, manf_day, manf_year = map(int,manf_date.split('/'))
    
#     expiry_month = manf_month + best_before_months
#     expiry_year = manf_year
#     expiry_day = manf_day

#     while expiry_month > 12:
#         expiry_month -= 12
#         expiry_year += 1

#     if (expiry_year > todays_year) or (expiry_year == todays_year and expiry_month > todays_month) or (expiry_year == todays_year and expiry_month == todays_month and expiry_day > todays_day):
#         return "Good to sale"
#     else:
#         return "Expired"

# def main():
#     while True:
#         print("Welcome to Kalyan's super market's inspection portal")
#         print("Today's Date is:12/01/22")
#         product_code = int(input("Enter the product code: "))
#         if product_code == 1:
#             pro_name = "Soap"
#             print(f"Product name: {pro_name}")
#             print(fun("01/02/22",12))
#         elif product_code == 2:
#             pro_name = "Shampoo"
#             print(f"Product name: {pro_name}")
#             print(fun("03/14/22",6))
#         elif product_code == 3:
#             pro_name = "Toothpaste"
#             print(f"Product name: {pro_name}")
#             print(fun("02/12/22",7))
#         elif product_code == 4:
#             pro_name = "Ready juice"
#             print(f"Product name: {pro_name}")
#             print(fun("11/08/22",2))
#         elif product_code == 5:
#             pro_name = "Chips"
#             print(f"Product name: {pro_name}")
#             print(fun("11/20/22",1))
#         else:
#             print("Enter a vlid name")

# main()

#Check location for product delivery

# import re 
# def fun():
#     dict = {"Bangalore" :560000, "Hyderabad" :50000,"Chennai" :600000,"Mumbai":400000}
#     city = input("Enter the full address or just city name: ")
#     parts = re.split(r'[,\s]+', city)
#     for part in parts:
#         ci = part.strip()
#     if ci in dict.keys():
#         print(f"Postal code is {dict[ci]}")
#         print("We can reach you in time...")
#     else:
#         print("Sorry! the product cannot be delivered to the address you are entering.")


# fun()

#Eva furniture center

# def fun(code,amount):
#     if code == 'CDEC01':
#         amount -= 500
#         print(f"successfully applied the coupon code: {code} please pay {amount}")
#     elif code == 'ONEJAN02':
#         amount = amount//2
#         print(f"successfully applied the coupon code: {code} please pay {amount}")
#     elif code == '2234150':
#         print(f"successfully applied the coupon code: {code}")
#         print(f"Congratulations! You got 1000 loyalty points for shopping with us. Please pay {amount}/-")
#     else:
#         print("Please Enter a valid cupon code")

# def main():
#     while True:
#         print("\nWelcome to online shopping")
#         print("your cart is not empty.")
#         print("You have to pay Rs. 1500/-")
#         choice = input("Do you have coupon? type y or n: ")
#         if choice == 'y':
#            code =  input("Please enter the coupon code: ")
#            fun(code,1500)
#         elif choice == 'n':
#            print("Please pay Rs. 1500/-")
#         else:
#            print("Enter valid option")

# main()



#Discount coupon

# dict = {
#     "pdcc01": {"name": "Chair", "price": 1500, "location": "B1R1C2", "quantity": 2},
#     "pdcs11": {"name": "Sofa", "price": 50000, "location": "B2R4C1", "quantity": "Home"},
#     "pdct25": {"name": "Table", "price": 15000, "location": "B3R3C2", "quantity": "Home"},
#     "pdcd011": {"name": "Desk", "price": 900, "location": "B4R2C3", "quantity": 13},
#     "pdcR012": {"name": "Shelf", "price": 2500, "location": "B5R1C4", "quantity": 0}
# }

# def fun():
#     while True:
#         code = input("\nEnter the product code: ")
#         if code in dict:
#             product = dict[code]
#             print(f"Product Type: {product['name']}")
#             if product['quantity'] == "Home":
#                 print(f"Price: {product['price']} + 600/- Rs. Delivery charge")
#                 print(f"Please pay Rs. {product['price'] + 600}")
#                 print("The product will be delivered to your home.")
#             elif product['quantity'] == 0:
#                 print(f"Product price: {product['price']}")
#                 print("Sorry! Out of stock")
#             elif product["quantity"] == 2 or 13:
#                 print(f"Product price: {product['price']}")
#                 print(f"You can collect the product in the ground floor, Bay: {product['location'][1]} Row: {product['location'][3]} Column: {product['location'][5]}")
#             else:
#                 print("enter valid code")
#         else:
#             print("Please enter a valid product code.")

    
# fun()



#Customer sign in

# import re  
# print("Please fill the details to sign in")
# name = input("Full Name: ")
# print("Delivery address:")
# l1 = input("Line 1: ")
# l2 = input("Line 2: ")
# l3 = input("Line 3: ")
# while True:
#   mail = input("Email id: ")
#   pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$'
#   if re.match(pattern,mail):
#      print(f"{mail}")
#      break
#   else:
#     print(f"Please enter a valid email ID: {mail}")
# while True: 
#    card = input("Card No: ")
#    if card.isdigit() and len(card) == 16:
#      print(card)
#      break
#    else:
#       print(f"Enter 16 digits card no.: {card}")
# while True:
#    gst = input("GST No: ")
#    pattern = r"^\d{2}[A-Za-z0-9]{10}\d{1}Z\d{1}$"
#    if re.match(pattern,gst):
#       print(gst)
#       break
#    else:
#      print(f"Enter a valid GST no.:{gst}")    
# print("Thank you")

#feedback

# name = input("Enter your name: ")
# product = input("Enter the product name: ")
# feedback = input("Write your feedback here and help us to improve the service: ")
# with open(f"{product}.txt",'a') as f:
#     f.write("Name:Feedback\n")
#     f.write(f"{name}:{feedback}\n")
#     f.close()
# print("Thank you for your valuable feedback on the product.")

#filter the red saree

#dict = {'s1':['red','Silk',4500],'s2':['blood red','Silk',11500],'s3':['pink','Silk',11200],'s4':['rose red','Party wear',6999],'s5':['lemon yellow','Silk',8500],'s6':['brick red','Silk',8500], 's7':['Green','Party wear',8999],'s8':['brick red','cotton',1500],'s9':['Candy red','Silk',8500],'s10':['Ruby red','Silk',9999],}
#x = list(map(lambda key: key, filter(lambda x: "red" in x[1][0] and x[1][1] == "Silk" and x[1][2] < 10000,dict.items())))
# lis = [i[0] for i in x]
# print(lis)

#find teddy bear

# s=input('Enter the name of products stored in the cotton box: ')
# x = s.split(',')
# lis = []
# for i in x:
#     if 'teddy' in i:
#         lis.append(i)
# print("Dear Surya,")
# print(f"Total {len(lis)} teddies are there. And, here they are:")       
# print(lis)

#loyality points

# dict={'Sajid':120,'Roopesh':85, 'Koushik':50, 'Lakshmi':64, 'Sathvik':12}
# name = input("Please enter the customer name: ")
# x = 0
# if name not in dict.keys():
#     print("New customer")
# else:
#     print("customer name",name)
# cupon = input("Do the customer has the coupon? Type y or n: ")
# if cupon == 'y':
#    code = int(input("Please enter the coupon code: "))
#    if code == 123476:
#        x = 20
#    else:
#        print("Invalid cupon code entered")
# bill = float(input("Enter the bill amount to be paid: "))
# points = bill//100
# if x==20:
#     points += 20
# if name in dict.keys():
#     points += dict[name]

# if points > 100:
#     bill -= 100
#     points -= 100
#     print(f"Congratulations! you won Rs. 100 cash back. You have to pay Rs.: {bill}")
# if name not in dict.keys() and cupon != 'y':
#     print(f"You have {int(points)} loyalty points in your account. Please pay Rs.: {bill} Thank you.")
# print(f"And remaining loyalty points in your account is: {int(points)}")

# import calander

# def fun(year,month):
#     first_weekday,days_in_month = calendar.monthrange(year, month)
#     cal = calendar.monthcalendar(year, month)
#     monday = [week[calendar.MONDAY] for week in cal if week[calendar.MONDAY] != 0]
#     x = list(c.month_name)
#     y = list(c.day_name)
#     if first_weekday == c.MONDAY:
#         print(f"{x[month]} 1 {year} is monday")
#         print(f"Your salary will credit on: {x[month]} - 1")
#     else:
#         print(f"{x[month]} 1 {year} is a {y[first_weekday]}. Next Monday is {x[month]} {monday[0]}")
#         print(f"Your salary will credit on this day: {x[month]} - {monday[0]}")


# y = int(input("Enter the year: "))
# m = int(input("Enter month: "))
# fun(y,m)

# dict = {
#     '100': {'name':'Deepthi','pin':1234,'balance':0},
#     '101': {'name':'Eva','pin':2345,'balance':100000},
#     '102': {'name':'Raghavendra','pin':3456,'balance':110000},
#     '103': {'name':'Sthuthi','pin':4567,'balance':85000},
#     '104': {'name':'Sujay','pin':5678,'balance':50500}
# }

# account_no = input("Please enter your Account no: ")
# if account_no in dict.keys():
#     pin_no = int(input("Please enter the 4 digit pin: "))
#     if pin_no == dict[account_no]['pin']:
#         print(f"Hi {dict[account_no]['name']}")
#         print(f"Your net balance is: {dict[account_no]['balance']}")
#     else:
#         print("Sorry Invalid Pin.")
# else:
#         print("Entering wrong account no. Please try again")
#         print("Please visit our bank and create an account")


# Customer name	Product name	Price in Rs.
# Narendra 	Toy1	Toy1 
# Sujata 	Pink saree 	7500
# Shritan 	T-shirt 	500

# import datetime
# dict = {'Narendra' : ['Toy1',499],'Sujata' : ['Pink saree',7500],'Shritan' : ['T-shirt',500]}

# print("Please enter the details to return the product.")
# name = input("Enter your name: ")
# if name in dict.keys() or name  not in dict.keys():
#     product = input("Enter the product name: ")
#     if product == dict[name][0]:
#         print("When did you purchase the product?")
#         user_date = input("Please enter the date in mm/dd/yy format: ")
#         user_date =user_date.replace('/','-')
#         date_ = datetime.datetime.strptime(user_date, "%m-%d-%y")
#         date_ = date_.date() 
#         today = datetime.date.today()
#         delta = datetime.timedelta(7)
#         past = today - delta
#         if date_ >= past:
#             print(f"Product: {dict[name][0]}  will be collected from the delivered address and amount: {dict[name][1]} will be returned to your account.")
#         else:
#             print("Sorry! the product cannot be returned")
#     else:
#         print("You have not purchased that product recently with us.")
# else:
#     print("You have not purchased that product recently with us.")

# print("Thank you")

#exception handling

# 1. Write a program to raise exception 
# a. enter name of the person raise exception where it is below 3 letters

# def fun(name):
#     if len(name) < 3:
#         raise TypeError("name should be more than 3 chars")
#     else:
#          print(f"Hello {name}")
# try:
#     name = input("Enter name:")
#     fun(name)
# except TypeError as e:
#         print(f"TypeError: {e}")

# b. enter salary of the person raise exception when salary below 10000
# def fun(salary):
#     if salary < 10000:
#         raise ValueError("The salary should be morethan 10000")
#     else:
#         print(f"salary: {salary}")
# try:
#     n = int(input("Enter salary: "))
#     fun(n)
# except ValueError as e:
#     print(f"valeError {e}")

# 2. Define your exception as UsernameLengthFailure 
# a. enter username if namelength is below 4 and above 8 raise exception

# class customError(Exception):
#     pass

# def fun(name):
#     if len(name) < 4 or len(name) > 8:
#         raise customError("name should be in limit")
# try:
#     name = input("Enter :")
#     fun(name)
# except customError as e:
#     print(f"customError: {e}")






