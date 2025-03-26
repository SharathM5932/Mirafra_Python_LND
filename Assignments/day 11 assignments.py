
class validation_error(Exception):
    pass
class Testdata:
    def test(self,name):
        if len(name)<3:
            raise validation_error()
    def testnum (self,num):
        if num<10000:
            raise validation_error()
name=input('Enter the name')
tes=Testdata()
try:
    tes.test(name)
except validation_error:
    print("Letter would not be smaller than 3")
else:
    num = int(input("Enter the salary"))
    try:
        tes.testnum(num)
    except validation_error:
        print("Salary should not be smaller than 10000")
    else:
        print("Successfully validated")


#-------------------------------------------------------------------------------------------------------

class UsernameLengthFailure(Exception):
    pass
class user_name:
    def len_check(self,name):
        if len(name)<4 or len(name)>8:
            raise UsernameLengthFailure()
name=input("Enter the name")
obj=user_name()
try:
    obj.len_check(name)
except UsernameLengthFailure:
    print("The Length of the name is neither below 4 nor above 8")
else:
    print("Successfully Accepted")


