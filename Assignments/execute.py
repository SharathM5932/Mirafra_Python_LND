#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# print(type(Node))
import time
# class A(type):
#     def __init__(cls,name):
#         name="anuroop"
#
# class B(metaclass=A):
#     print(name)
#     name="anuroop1"
# class MyMeta(type):
#     def __init__(cls, name, bases, dct):
#         print(f"Initializing class {name}")
#         super().__init__(name, bases, dct)
#
# class MyClass(metaclass=MyMeta):
#     print(name)


# Output: Initializing class MyClass

# for i in range(5):
#     print(i)
# else:
#     print("Loop finished without interruption.")

# from abc import ABC,abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return "barke"
#     def move(self):
#         return "4"
# class Bird(Animal):
#     def speak(self):
#         return "sound"
#     def move(self):
#         return "fly"
# b1=Bird()
# d1=Dog()
# print(d1.move())
# print(b1.speak())
from abc import ABC,abstractmethod
# class Bankaccount:
#     def __init__(self,acc_no,acc_hol,balance):
#         self.acc_no=acc_no
#         self.acc_hol=acc_hol
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=amount+self.balance
#
#     def withdraw(self,amount):
#         self.balance=self.balance-amount
#
#     def p(self):
#         print(self.balance)
#
# a1=Bankaccount(1,"anu",100)
# a1.deposit(100)
# a1.p()
# a1.withdraw(20)
# a1.p()

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class tri(shape):
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         print(self.side*self.side)
# t1=tri(100)
# t1.area()

# lst=[1,2,34,4]
# print(lst.insert(-20,10))
# print(lst)

#
# def anuroop():
#     yield 1
#     yield 2
#
# for i in anuroop():
#     print(i)

# class anuroop:
#     def __init__(self):
#         self.number=0
#     def __iter__(self):
#         self.number=1
#         return self
#     def __next__(self):
#         self.number+=1
#         return self.number
# a=anuroop()
# iter(a)
# print(next(a))
# print(next(a))

# import threading
# def a1():
#     for _ in range(2):
#         print("a")
#         time.sleep(1)
# def b1():
#     for _ in range(2):
#         print("b")
#         # time.sleep(1)
# t1=threading.Thread(target=a1)
# t2=threading.Thread(target=b1)
# t1.start()
# t2.start()

# a=set()
# a.add(1)
#
# b=iter(a)
# print(next(b))
#
# s='rohit'
# s1='tihor'
# if set(s) == set(s1):
#     print('yes')
# flag=True
# while flag:
#     try:
#         n=int(input(":"))
#         flag=False
#     except:
#         print("enter integer")
# print(n)

# with open("C:\\Users\\User\\OneDrive\\Desktop\\1.txt", 'r') as f:
#     s = f.readline()
#     print(s)

# lst=[x for x in range(1,10) if x%2==0]
# print(lst)

# with open('anuroop1','w') as f:
#     f.write("anuroop sharath anur anuroop")
#
# with open('anuroop1','r+') as f:
#     a=f.readline()
#     print(type(a))
#     if a.strip() =='anuroop':
#         f.seek(0)
#         f.write('sharath')
#         f.truncate()

# str1='bengaluru, my name is bengaluru banglore'
# str2='bengaluru'
# import re
# str1=re.sub(str2,"mysuru",str1)
# print(str1)
# lst2=str1.split(" ")
# print(lst2)
# print("".join(map(str,lst2)))

# lst=[4,7,1,4,5,2,1]
# mini1=lst[0]
# mini2=lst[1]
# if mini1>mini2:
#     mini1,mini2=mini2,mini1
# for i in range(2,len(lst)):
#     if lst[i]<mini2:
#         mini2=lst[i]
#         if mini1>mini2:
#             mini1, mini2 = mini2, mini1
# print(mini2)

# str1="geeksforgeeks"
# count=0
# for i in str1:
#     if i.is:
#         count+=1
# print(count)
# str2=""
# for i in str1:
#     if i not in str2:
#         str2+=i
# print(str2)
# str1="abcabcedfhibb"
# lst=[]
# count=0
# new_count=0
# for i in str1:
#     if i not in lst:
#         lst.append(i)
#         count+=1
#     else:
#         new_count=max(count,new_count)
#         count=0
# print(new_count)

# str2="({[]})"
# st=[]
# blst="]})".split()
# for i in str2:
#
#     if len(st)==0:
#         st.append(i)
#     elif i==:
#         print(st[-1])
#         st.pop()
#     else:
#         st.append(i)
#     print(i, st[-1])
# if len(st)==0:
#     print("s")








# lst1=lst[:2]
# for i in range(2,len(lst)):
#     lst1.append(lst[i])
#     lst1.sort()
#     # lst1.append(lst[i])
#     print(lst1.pop(-1))
# print("--",lst1[1])



# n=153
# sum1=0
# while n!=0:
#     rem = n % 10
#     n=n//10
#     print(n)
#
#     print(rem)
#     sum1+=rem**3
# print(sum1)

# sr='anuroop'
# sa="pooruna"
# lst1=list(sr)
# lst2=list(sa)
# print(lst2.sort())

# class anuroop:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
# print(anuroop.add(2,3))

# num=100
# flag=True
# for i in range(2,int(num**0.5)):
#     if num%i==0:
#         print("not prime")
#         flag=False
#         break
# if flag:
#     print("is prime")

# def fibo(num):
#     n1 = 0
#     n2 = 1
#     print(n1)
#     print(n2)
#     for _ in range(num-2):
#         n1,n2=n2,n1+n2
#         print(n2)

str1="mississippppppi"
count=0
lst=[]
for i in str1:
    if i not in lst:
        lst.append(i)
        new_count=str1.count(i)
        if new_count>count:
            c=i
            count=max(count,new_count)
print(c)


# fibo(6)





