#Customer sign in
#As you know everyone has to sign in by giving valid details to any online shopping site to shop. So that these data will be stored in shopping site permanently which will help sellers to know their customers better and customers need not to enter their details.
#Being a programmer write a program which will act as:
#1.	A sign in form which will take the basic details of a customer
#2.	Validate the data entered
#3.	If the data entered is wrong ask the customer to re-enter  n no. of times until they enter a valid data.
#4.	Finally accept only the valid data.
#Conditions for valid fields:
#1.	Full name.
#2.	Address: in 3 lines
#3.	Email: A email ID  should have ‘@’ symbol and a domain name to be valid.
#4.	Card:16 digits
#5.	GST no.:8 digit and 7 alphabets

import re
def full_name(fullname):
    if len(fullname)>0:
        return True
    else:
        return False
def address(address1):
    if len(address1)==3:
        return True
    else:
        return False
def email(email_id):
    email1=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email1,email_id):
        return True
    else:
        return False
def card(card_no):
    if len(card_no)==16 and card_no.isdigit():
        return True
    else:
        return False
def gst(gst_no):
    gst1=r'^[0-9]{2}[A-Za-z]{5}[0-9]{4}[A-Za-z]{1}[0-9]{1}[A-Za-z]{1}[0-9]{1}$'
    if re.match(gst1,gst_no):
        return True
    else:
        return False


i=1
while i<10:
    print("Sample case {}:".format(i))
    print("Please fill the details to sign in.")
    while True:
        fullname=str(input("Full Name: "))
        if full_name(fullname):
            break
        else:
            print("Invalid name")
    while True:
        print("Delivery Address:")
        address1 = []
        for x in range(1, 4):
            line = input("Line {}:".format(x))
            address1.append(line)
        if address(address1):
            break
        else:
            print("Please Enter Address:")
    while True:
        email_id = input("Email Id:")
        if email(email_id):
            break
        else:
            print("Please Enter the valid Email:")

    while True:
        card_no = input("Card no.:")
        if card(card_no):
            break
        else:
            print("Please Enter Valid Card No:")
    while True:
        gst_no = input("GST No:")
        if gst(gst_no):
            break
        else:
            print("Please Enter the valid GST No:")
    print("Thank You")
    i += 1



