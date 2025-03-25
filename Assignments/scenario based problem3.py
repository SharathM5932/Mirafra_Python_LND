# scenario1
'''dict1={"sajid":122,"roopesh":115,"anuroop":50}
name=input("Please enter the customer name:").lower()
if not name in dict1:
    print("New customer")
    choice=input("Do the customer has the coupon? Type y or n:").lower()
    match choice:
        case "n":
            amount=int(input("Enter the bill amount to be paid:"))
            points=amount//100
            dict1[name]=points
            print(f"You have {points} loyalty points in your account. Please pay Rs.: {amount}.0 Thank you.")
        case "y":
            code=input("Please enter the coupon code:")
            amount = int(input("Enter the bill amount to be paid:"))
            points = (amount // 100)+20
            cashback=0
            while points>100:
                cashback+=100
                points-=100
            dict1[name] = points
            if cashback>0:
                print(f"Congratulations! you won Rs. {cashback} cash back. You have to pay Rs.:  {amount-cashback}.0")
                print(f"And remaining loyalty points in your account is: {points}")

else:
    print("Customer name",name)
    choice = input("Do the customer has the coupon? Type y or n:").lower()
    match choice:
        case "n":
            amount = int(input("Enter the bill amount to be paid:"))
            cashback = 0
            points=dict1[name]
            while points > 100:
                cashback += 100
                points -= 100
            dict1[name] = points
            if cashback > 0:
                    print(f"Congratulations! you won Rs. {cashback} cash back. You have to pay Rs.:  {amount - cashback}.0")
                    print(f"And remaining loyalty points in your account is: {points}")
            else:
                while amount>=100:
                    points+=1
                    amount=amount//2
                print(f"You have to pay Rs.:  {amount - cashback}.0")
                print(f"And remaining loyalty points in your account is: {points}")
        case "y":
            code = input("Please enter the coupon code:")
            amount = int(input("Enter the bill amount to be paid:"))
            print(dict1[name])
            dict1[name] += (amount // 100) + 20
            points=dict1[name]
            print(points)
            cashback = 0
            while points > 100:
                cashback += 100
                points -= 100
            dict1[name] = points
            if cashback > 0:
                print(f"Congratulations! you won Rs. {cashback} cash back. You have to pay Rs.:  {amount - cashback}.0")
                print(f"And remaining loyalty points in your account is: {points}")'''
from streamlit import feedback

# scenario2================
'''str1=input("Enter the name of products stored in the cotton box:")
lst=str1.split(",")
pattern="teddy"
lst1=[]
import re
for item in lst:
    if re.search(pattern,item):
        lst1.append(item)
print("Dear Surya,")
print(f"Total {len(lst1)} teddies are there. And, here they are:")
print(lst1)'''

# scenario3============================
'''name=input("Enter your name:")
product=input("Enter the product name:").lower()
product=product.replace(" ","")
with open(product,'a') as f:
    print("Write your feedback here and help us to improve the service:")
    feed=input()
    f.write("\n"+name+" says: "+feed)
    print("Thank you for your valuable feedback on the product.")

# with open(product,'r') as f:
#     for i in f.readlines():
#         print(i[1])
'''
# scenario4===================
import re
def find_red(str4):
    if re.search("red",str4):
        return True
    return False



dict4=eval(input("Enter the product details to store it into our data base:"))
lst4=[]

for key in dict4.keys():
    if find_red(dict4[key][0]) and dict4[key][1]=='Silk' and dict4[key][2]<10000:
        lst4.append(key)
print(lst4)

# lst5=list(filter(lambda key:"red" in dict4[key][0] and dict4[key][1]=="Silk" and dict4[key][2]<10000,dict4))
# print(lst5)


