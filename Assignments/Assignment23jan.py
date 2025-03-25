"""1. Write a program to raise exception
a. enter name of the person raise exception where it is below 3 letters
b. enter salary of the person raise exception when salary below 10000

2. Define your exception as UsernameLengthFailure
a. enter username if namelength is below 4 and above 8 raise exception"""

name=input("Enter name :")
l=len(name)
try:
      if l<=3:
         raise NameError(l)
except NameError:
    print("OHHHH too short Name")
salary=int(input("Enter Salary:"))
try:
    if salary <=10000:
        raise ValueError(salary)
except ValueError:
    print("Too less amount Entered.")
else:
    print("okay")


class UsernameLengthFailure(Exception):
    pass
class TestData:
    def testMe(self, m):
        if (m>=4 and m<=8):print('validation successful')
        else:raise UsernameLengthFailure('Validation Failed')
#once you declare variable for TestData class as follows:
test =TestData()
username=input("Enter username:")
m=len(username)
test.testMe(m)