data={
    100:["Deepthi",1234,0],
    101:['Eva',2345,100000],
    102:['Raghavendra',3456,110000],
    103:['Sthuthi',4567,85000],
    104:['Sujay',5678,50500]
}
acc_no=int(input("Please enter your Account no.:"))
if acc_no in data.keys():
    pin=int(input("Please enter the 4 digit pin:"))
    if pin==data[acc_no][1]:
        print(f"Hi {data[acc_no][1]}")
        print(f"Your net balance is:{data[acc_no][2]}")
    else:print("Sorry invalid pin")
else:print("Entering wrong account no. Please try again.\nPlease visit our bank and create an account.")