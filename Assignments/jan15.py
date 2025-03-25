"""class MyClass():
    x=10
p=MyClass
print(p.x)

class MyClass:
    x=15
p=MyClass()
print(p.x)

class MyClass():
    x=20
p=MyClass()
print(p.x)

class MyClass:
    x=5
p=MyClass
print(p.x)"""

#class Sample:
 #   """ This is a Sample Class"""
  #  pass
#x=Sample
#print(x.__doc__)"""

#class Man():
 #   """This is a class"""
  #  age=12
   # def greet(self):
    #    print("hello")
#print(Man.age)
#print(Man.greet(0))
#print(Man.__doc__)

"""class Calculate:
    @staticmethod
    def addNumbers(x,y):
        return x+y
c=Calculate.addNumbers(2,3)
print(c)
"""

"""class Calculate:
    def addNumbers(x,y):
        return x+y
c=staticmethod(Calculate.addNumbers(12,34))
print(c)"""


"""class A:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def concat(self):
        return self.lname+self.fname
    def methodA1(self):print("I'm from A1")
    def methodA2(self):print("I'm from A2")
class B(A):
    def methodB1(self):print("I'm from B1")
    def methodB2(self):print("I'm from B2")
class C(B):
    def methodC1(self):print("I'm from C1")
    def methodC2(self):print("I'm from C2")
c=C(" radha","g")
c.methodC1()
c.methodB1()
c.methodA2()
print(c.concat())
"""


"""class A:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def concat(self):
        return self.lname + self.fname

    def methodA1(self):print("I'm from A1")
    def methodA2(self):print("I'm from A2")
class B:
    def methodB1(self):print("I'm from B1")
    def methodB2(self):print("I'm from B2")
class C(A,B):
    def methodC1(self):print("I'm from C1")
    def methodC2(self):print("I'm from C2")
c=C("Radha","G")
c.methodC1()
c.methodA2()
c.methodB2()
print(c.concat())"""



