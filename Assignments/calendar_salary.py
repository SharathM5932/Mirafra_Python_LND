import calendar
from datetime import date
year=int(input("Enter The Year:"))
month=int(input("Enter the month:"))
due=1
for month in range(1,13):
    month_calender = calendar.monthcalendar(year, month)
    due_date = date(year, month, due)
    for day in month_calender:
        if day[calendar.MONDAY]!=0:
            monday_date=date(year,month,day[calendar.MONDAY])
            delay=monday_date-due_date
            print("Your Salary Will Credit on Monday:{} and Delay:{}".format(monday_date,delay))
            break