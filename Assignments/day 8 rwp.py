import os
name=input("Enter your name:")
prd_name=input("Enter the product name:")
feedback=input("Write your feedback here and help us to improve the service:\n")
print("Thank you for your valuable feedback on the product.")
if os.path.exists(prd_name):
    with open(prd_name,'a') as file:
        file.write(f"{name} says: {feedback}\n")
else:
    with open (prd_name,'w') as file:
        file.write(f"{name} says: {feedback}\n")

with open (prd_name,'r') as file:
    print(file.read())

#----------------------------------------------------------------------------------------

product=input("Enter the name of products stored in the cotton box:")
lst=product.split(',')
count=0
main_list=[]
for i in lst:
    if 'teddy' in i.lower():
        main_list.append(i)
        count+=1
print(f"Dear Surya,\nTotal {count} teddies are there. And, here they are:\n{main_list}")

#-------------------------------------------------------------------------------------------------

dic=eval(input("Enter the product details to store it into our data base:\n"))
lis=list(filter(lambda n:'red' in dic[n][0] and dic[n][1]=='Silk' and dic[n][2]<=10000 ,dic))
print(lis)

#--------------------------------------------------------------------------------------------------


