# login.py

import re

def email_check(email_ID):
    reg_mail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\x.(com|org|net|gov|edu|in|co|us|info|io)'
    return re.match(reg_mail, email_ID) is not None

def card_check(Card_no):
    return len(str(Card_no)) == 16

def gst_check(GST_no):
    reg_pat = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9]{1}[A-Z0-9]{1}[Z]{1}[0-9]{1}$'
    return re.match(reg_pat, GST_no) is not None

def login():
    print("Please fill in the details to sign in.\n")
    name = input("Full Name: ")
    print("Delivery address:\n")
    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")

    email_ID = input("Email ID: ")
    while not email_check(email_ID):
        email_ID = input("Please enter a valid email ID: ")

    Card_no = input("Card no: ")
    while not card_check(Card_no):
        Card_no = input("Enter 16 digits card no: ")

    '''GST_no = input("GST no: ")
    while not gst_check(GST_no):
        GST_no = input("Enter a valid GST no: ")'''

    print("Thank you for signing in.")
