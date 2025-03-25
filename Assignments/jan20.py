"""import math
print(math.ceil(-32.1))
print(math.ceil(5.1))
print(math.ceil(5.9))
"""
"""c=7
print(c.__ceil__())"""

"""import math
print(math.floor(7))
print(math.floor(7.9))
print(math.floor(7.1))
print(math.floor(-0.5))#=-1
c=444
print(c.__floor__())"""
import math
"""print(math.copysign(3.4,0.0))
print(math.copysign(3.4,-7.8))
math.copysign(-3.4,-7.8)"""


#print(math.factorial(5))

"""print(math.isnan(5))
print(math.isnan('geeta'))"""

"""print(math.lcm(3,13))
print(math.gcd(3,13))"""
"""a=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
print(math.fsum(a))
sum(a)"""

#print(round(1.5))
#print(round(10.5))
#print(round(20.5))

"""import sys
sys.stdout.write('deeps')"""

"""import sys
def print_to_stderr(*a):
    # Here a is the array holding the objects
    # passed as the arguement of the function
    print(*a, file = sys.stderr)
print_to_stderr("Hello World") """

"""import sys
age = 19
if age < 18:
    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
print('bye')"""

"""import sys
print(sys.modules)"""
import sys
#print(sys.getrefcount(0))

"""a = 5
print(sys.getrefcount(a))"""
"""import sys
print(sys.version)
print(sys.argv) """

import random
"""list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
string = "striver"
print(random.choice(string))"""

"""print(random.random())
random.seed(7)
print("The mapped random number with 5 is : ", end="")
print(random.random())"""

"""sample_list = ['A', 'B', 'C', 'D', 'E']
random.shuffle(sample_list)
print(sample_list)"""

"""random.randint(1,10)
random.randrange(stop)
random.randrange(1,10,2)"""

"""import os
'''os.chdir('C:\\Users\\S KRISHNA\\PycharmProjects\\mypython project')
print(os.getcwd())'''
os.mkdir('dir1')
#os.rmdir('dir1')"""

a,b=45000,10
'''from dir1.file1 import increment
from dir1.file2 import cut
import dir1.file1
import dir1.file2
import file1,file2
import dir1.file1 as f1
import file2
from file1 import increment,cut
from file1 import increment
from file1 import cut'''


from datetime import date
from datetime import datetime
from datetime import time

"""i=date.today()
print("today's date is:",i)"""

"""i=date.today()
print("today's date is:",i.day, i.month, i.year,i.weekday())"""

"""i=datetime.time(datetime.now())
print("today's date is:",i)"""

"""i=datetime.now()
print(i.strftime("%a,%d,%b,%y"))"""

"""i=datetime.now()
print(i.strftime("%A,%d,%B,%Y"))"""

"""i=datetime.now()
print(i.strftime("%c"))
print(i.strftime("%x"))
print(i.strftime("%X"))"""

"""from datetime import datetime
from datetime import timedelta

i=datetime.now()
print("today:",i)
print(timedelta(days=365, hours=8, minutes=45))
print("one year from now:" + str(datetime.now() + timedelta(days=365)))
"""

"""from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
import time
import datetime
print(datetime.datetime.today())
#from how long I'm using PyCharm in secs
print(time.time())
print(time.localtime())
print(date.today())
#print(datetime.now())'''
i=date.today()
print("today'd date is:", i.day,'/',i.month, i.year,i.weekday())
i=datetime.datetime.now()
print(i.strftime("%a, %d, %b, %y"))
print(i.strftime("%A, %d, %B, %Y"))
print(i.strftime('%c'))
print(i.strftime('%x'))
print(i.strftime('%X'))
i=datetime.datetime.now()
print('today:',i)
print(timedelta(days=365,hours=8,minutes=45))
print('one year from now:'+str(datetime.datetime.now()+timedelta(days=455,hours=3)))"""

import salary
'''a=calendar.TextCalendar(calendar.MONDAY)
b=a.formatmonth(2019,1)
print(b)
year=2020
print(calendar.calendar(1989))'''
import salary
for i in calendar.month_name: print(i)
a=calendar.TextCalendar(calendar.MONDAY)

for i in a.itermonthdays(2012,2): print(i)
a=calendar.HTMLCalendar(calendar.MONDAY)
b=a.formatmonth(2019,1)
print(b)

