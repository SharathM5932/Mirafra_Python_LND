# class base(object):
#     def __init__(self,name):
#         self.name=name
#
#     def getname(self):
#         return self.name
#
# class child(base):
#     def __init__(self,age,name):
#         base().__init__(self,name)
#         self.age=age
#     def getage(self):
#         pint("dwuh")
#         return self.age
# obj=child(21,"anuroop")
# print(obj.getname())
#

# class C:
#     def __init__(self):
#         self.c = 21
#         self.__d = 42
#     def func(self):
#         print(self.__d)
# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)
#     def func(self):
#         print(self.c)
# object1 = C()
# object1.func()

class A:
    def __init__(self):
        self.a=1
        self._b=2
        self.__c=3
    def func(self):
        self.__c=10
        print(self.a,self._b,self.__c)

class B:
    def __init__(self):
        A.__init__(self)
        self.d=4
    def func(self):
        self._b=10
        print(self.a,self._b,self.__c)

obj=A()
obj.func()

# overloading-eg len biltin

class bill:
    def __init__(self,m,u):
        self.m=m
        self.u=u
    def __add__(self,other):
        m=self.m-other.m
        u=self.u-other.u
        bill1=bill(m,u)
        return bill1
    def __gt__(self,others):
        print(self.m,self.u)
        if self.m!=self.u:
            return "false"
        else:
            return "true"


# a1=bill(70,30)
# a2=bill(40,50)
# a=a1+a2
# b=a>a
# print(b)
# if b:
#     print("my bill greater your bill")
# else:
#     print("my bill greater your bill")

# gettattr(2 args-class name,attribute in str "")[only for attributes]
# settattr(3 args-class name,attr in str,changes)[only attr]

#

