from datetime import date,timedelta
import datetime



def returnme(name,product,datep):
    dict1 = {"Narendra": ['Toy1', '01/18/25', 499],
             "Shritan": ['T-shirt', '01/01/25', 500]}
    if name in dict1 and product==dict1[name][0]:
        if datep==dict1[name][1]:
            date_g=str(date.today())
            date1=datetime.date(int(date_g[2:4]),int(date_g[5:7]),int(date_g[8:]))
            date2=datetime.date(int(dict1[name][1][6:]),int(dict1[name][1][:2]),int(dict1[name][1][3:5]))
            if date1-date2<=timedelta(days=7):
                return f"Product:{dict1[name][0]} will be collected from the delivered address and amount:{dict1[name][2]} will be returned to your account."
            else:
                return "Sorry! the product cannot be returned"
        else:
            return "You have not purchased that product recently with us."
    else:
        return "You have not purchased that product recently with us."



