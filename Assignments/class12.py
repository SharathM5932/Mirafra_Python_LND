#1
class example:
    def greet(self):
        print("hello")
ex1=example()
ex2=example()
print(ex1,ex2)
ex1.greet()
ex1.id=1
ex1.name='halla'
ex2.id=2
ex2.name='bol'
a=example()
a.greet()
print(ex1.name,ex2.name)


#2
class example1():
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name

    def info(self):
        return f'{self.id} {self.name}'

emp1=example1(1,'deepthi',40000)
emp2=example1(2,'sthuthi',50000)
print(emp1.name)
print(emp2.name)
print(emp1.info())

#3
class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass

class Person(MyNewClass):
    '''this is a doc string'''
    age = 10
    def greet(self):
        print('Hello')
p1=Person()
print(Person.age)
print(Person.greet)
print(p1.__doc__)
harry = Person()
harry.greet()

#4 use of class method and static method.
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, lname,fname, year):
        name=lname+fname
        return cls(name,date.today().year - year)
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank',' xyz', 1996)
print (person1.name,person1.age)
print (person2.name,person2.age)
print (Person.isAdult(12))

class creature:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    def speak(self):
        print(f"speak{self.sound}")
class animal(creature):
    def which(self):
        print(f"name: {self.name}")
    d=creature('dog','bak')
    print(f"bye{d.name}")
a=animal('dog','bark')
a.speak()
a.which()


