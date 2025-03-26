from datetime import date,timedelta
def returnme(name,product,pd):
    td=date.today()
    data={
        "Narendra":["Toy1",300],
        'Sujata':["Pink saree",7500],
        "Shritan":["T-shirt",500]
    }
    if name in data.keys() and product == data[name][0]:

        month,day,year = map(lambda x: int(x), pd.split('/'))
        year=2000+year
        p_d=date(year, month, day)
        print(type(p_d))
        diff=(td-p_d)
        print(diff.days)
        if diff==timedelta(days=7):
            print(f"Product:{product}will be collected from the delivered address and amount:{data[name][1]} will be returned to your account")
        else:
            print("Sorry! the product cannot be returned")
    else:print("You have not purchased that product recently with us.")
    return "Thank you"

a=returnme('Sujata',"Pink saree","01/14/25")
print(a)
