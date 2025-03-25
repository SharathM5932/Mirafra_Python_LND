x={'Bangalore':560000,'Hyderabad':500000,'Chennai':600000,'Mumbai':400000}
data=input("enter full address: ")
for i in x:
    if i in data:
        print(x[i])
        print("Reach in time")
        break
else:
    print("sorry")



