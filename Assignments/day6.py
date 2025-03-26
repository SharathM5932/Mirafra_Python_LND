# class abhi:
#     print('hi')
# print(abhi)
# print(abhi())

# class abc:
#     def method1():
#         return('hi')
# print(abc.method1())
#
# object1=abc
# object2=abc
# print(type(object1))
# print(type(abc()))
# a=object1.method1
# print(a())

# class deepthi():
#     def method1(self):
#         print("hello")
# emp1=deepthi
# emp2=deepthi
# emp1.id=1
# emp1.name='deepthi'
#
# emp2.id=2
# emp2.n

# class complexNumber:
#     def __init__(self,i,j):
#         self.i=i
# #         self.j=j
# #     def get_num(self):
# #         print(f'{self.i}+{self.j}j')
# #
# # num1=complexNumber(1,2)
# # num1.get_num()
#
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass
# class Human(Animal):
#     def move(self):
#         print("I can walk and run")
#     def abhi(self):
#         print("hello")
# class Snake(Animal):
#     def move(self):
#         print("I can crawl")
# class Dog(Animal):
#     def move(self):
#         print("I can bark")
# class Lion(Animal):
#      def move(self):
#         print("I can roar")
#
# for i in Lion(),Dog():
#     i.move()

# class bill:
#     def __init__(self,m,u):
#         self.u=u
#         self.m=m
#
#     def __add__(self,other):
#         m=self.m+other.m
#         u=self.u+other.u
#         bill1=bill(m,u)
#         return bill1
#
#     def __gt__(self,other):
#         bill1 = self.m + other.m
#         bill2 = self.u + other.u
#         if bill1>bill2:
#             return('m is greater')
#         else:
#             return('u is greater')
#
#
#
# a1=bill(5000,5000)
# a2=bill(25000,10000)
# a=a1+a2
# print(a.m)

class A:
  _z = 100
  def __init__(self):
    self.a=1
    self._b=2
    self.__c=3

class B(A):
  def __init__(self):
    super().__init__()
    print(self._z)




b = B()
b._z = 10
# c=B()
# c._z = 20

