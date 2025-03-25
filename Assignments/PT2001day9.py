# # re module, re.subn, Flag setting, re.escape,
# math module-math.ceil(),.floor(),copysign(),.fsum(),.round() [imp] for 2 and 10 muliples it will not round off to next like 2.5-2,10.5-10 else 6.5-7
# sys module -sys.exits()/red color o/p,.version,.argv-gives the path
# random module - random.seed(),randint(),randrange(stop),randrange(start,stop,steps), random.shuffle()
# os.chdir(),mkdir(),rmdir()
# datetime- timedelta, strftime()
# calander
# # re.compile - is used to compile into a re eg:pattern=re.compile('ab") then pattern.sub/matc etc("string")
# import re
# s1=re.subn('[a-z]','#','a1due2hdu2678')
# print(s1)
#
# x1='''ptybib
# hciwhs
# cisih'''
# r1=re.findall('^\w',x1,re.MULTILINE)
# print(r1)
#
# x1='''Python
# hciwhs
# cisih'''
# r1=re.findall('python ',x1,re.IGNORECASE)
# print(r1)
#
import calendar
import math
# print(math.ceil(-32.1))
# print(math.ceil(5.1))
# print(math.ceil(5.9))

#floor() method in Python returns the floor of x i.e., the smallest integer not lesser than x.
# import math
# print(math.floor(7))
# print(math.floor(7.5))
# print(math.floor(7.1))
# print(math.floor(-0.5))#=-1
# c=444
# print(c.__floor__())

#copysign
# print(math.copysign(3.4,0.0),math.copysign(3.4,-7.8),math.copysign(-3.4,-7.8))

# a=[1,2,3]
# print(id(a))
# a.append(6)
# print(id(a))
#
# import os
# print(os.getcwd())
# os.mkdir("")

from datetime import datetime
# take year as input
# print the first mon date and days to wait for the salary

# import calendar
# # a=calendar.calendar(2024)
#
# b=calendar.month(2024)
# print(b)

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
# p1=person("anur",25)
# # print(getattr(p1,"age"))
# print(p1._person__age)

from datetime import datetime
import calendar
year=2025
count=0
# print(calendar.calendar(year))
for i in range(1,13):
    firstday=datetime(year,i,1)
    day=firstday.strftime("%A")
    day_no=firstday.weekday()

    if day_no!=0:
        count+=(7-day_no)
        print(day, day_no,"days to wait:",7-day_no)
    else:
        print(day, day_no)
print("total days to waited",count)

