import re

def email_check(email_ID):
    reg_mail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(reg_mail, email_ID) is not None
