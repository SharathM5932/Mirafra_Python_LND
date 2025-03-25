#1. Write a program to raise exception
#a. enter name of the person raise exception where it is below 3 letters
#b. enter salary of the person raise exception when salary below 10000

name=input("Enter your name: ")

try:
    if len(name)<3:
        raise NameError(name)
except NameError:
    print(name,"is very short")
else:
    print("Nice Name :)")
salary=int(input("Enter your Salary: "))
try:
    if salary<10000:
        raise ValueError(salary)
except ValueError:
    print(salary,"your salary is very low!...")
else:
    print("Bye!...")




#2. Define your exception as UsernameLengthFailure
#a. enter username if namelength is below 4 and above 8 raise exception

username=input("Enter your name: ")
class  UsernameLengthFailure(Exception):
    pass
class TestData:
    def testMe(self,username):
        if len(username)<8 and len(username)>4:
            print("User name Success")
        else:
            raise UsernameLengthFailure('Username Failure')
test =TestData()
test.testMe(username)
"""try:
    test.testMe('Deepika')
except UsernameLengthFailure:
    print('Validation Failed')"""