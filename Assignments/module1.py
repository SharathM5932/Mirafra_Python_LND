from datetime import datetime,timedelta

def returnme(product,date,sample):
    original_date = datetime.strptime(date, '%d/%m/%y')
    new_date = original_date + timedelta(days=7)
    if new_date>=datetime.today():
        print("Product:{} will be collected from the delivered address and amount:{} will be returned to your account.".format(product,sample))
        print("Thank you")
    else:
        print("Sorry! the product cannot be returned")
        print("Thank you")

