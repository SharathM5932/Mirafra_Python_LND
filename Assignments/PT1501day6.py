# ===================CLASS=======================================
'''class demo:
    def __init__(anuroop,name,age):
        anuroop.name=name
        anuroop.age=age
    def func(gowda):                           #self name can be changed should be accessed with the same name declared
        print("name:",gowda.name)

d1=demo('anuroop',20)
d1.func()'''

'''class demo:
    def info(self):
        print("hello",self.id)

d1=demo()
d2=demo()         # we can also init the attributes outside the class but with out security
d1.id=1
d2.id=2
print(d1.id)
d1.info()
print(d2.id)
d2.info()'''

# class,object,attributes and functions can be deleted but if an object is already created it will remain
# ================INHERITENCE=========
'''class animal:
    print("com")
    def speak(self):
        print("speak")   #if the parent is not mentioned then the flow goes to the animal for debugging not for init
class dog():
    def bark(self):
        print("bark")
d=dog()
d.bark()'''
# ===method1 to access using class animal==============
'''class animal:
    def speak(self):
        print("speak")
class dog():
    animal().speak()
    def bark(self):
        print("bark")
d=dog()
d.bark()'''

# ===method2 to access using super==============
# class animal:
#     def speak(self):
#         print("speak")
# class dog(animal):
#     super().speak()
#     def bark(self):
#         print("bark")
# d=dog()
# d.bark()

class abc:
    def meth1():
        return("hi")

obj1=abc
print(obj1.meth1())






