dic={100:['Deepthi',1234,0],101:['Eva',2345,100000],102:['Raghavendra',3456,110000],103:['sthuthi',4567,85000],104:['Sujay',5678,50500]}
acc=int(input("Please enter your Account no.:"))
for key,value in dic.items():
    if acc==key:
        pin=int(input("Please enter the 4 digit pin:"))
        if pin==value[1]:
            print(f"Hi {value[0]}\nYour net balance is {value[2]}")
            break
        else:
            print("Sorry Invalid Pin")
            break
else:
    print("Entering wrong account no. Please try again.\nPlease visit our bank and create an account.")

#_____________________________________________________________________________________________
import os
import datetime
def ffd(fpath):
    if not os.path.exists(fpath):
        print("The specified folder does not exist.")
        return
    for file in os.listdir(fpath):
        floc = os.path.join(fpath, file)
        if os.path.isfile(floc):
            cretime = os.path.getctime(floc)
            credate = datetime.datetime.fromtimestamp(cretime).strftime('%Y-%m-%d %H:%M:%S')
            fext = os.path.splitext(file)[1]
            print(f"File: {file}")
            print(f"Creation Date: {credate}")
            print(f"Extension: {fext}")
            print("-" * 40)
fpath = "C:\\Users\\User\\PycharmProjects\\PythonProject"
ffd(fpath)
#-----------------------------------------------------------------------------------------------
from datetime import date
name=input("Please enter the details to return the product.\nEnter your name")
dic={"Narendra":["Toy1",499],"Sujata":["Pink saree",7500],"Shritan":["T-shirt",500]}
if name in dic.keys():
    pdname=input("Enter the product name:")
    if pdname == dic[name][0]:
        print("When did you purchase the product?")
        dat= str(date.today())
        dat=int(dat.split('-')[2])
        predate=input("Please enter the date in mm/dd/yy format:")
        predate=int(predate.split('/')[1])
        if dat - predate>7:
            print(f"Product:{pdname} will be collected from the delivered address and ammount:{dic[name][1]} will be returned to your account.")
        else:
            print("Sorry! the product cannot be returned")
    else:
        print("You have not purchased that product recently with us.")
else:
    print("You have not purchased that product recently with us.")
print("Thank you.")



