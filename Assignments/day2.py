# exit- exit from program
# break- exit from loop
# n=1.1
# i=0.1
#
# while n<=5:
#     if type(n)==int:
#         print(n)
#         n+=i
#         continue
#         while n<=5:
#             print(n)
#             continue

# fruits = ["apple", "banana", "cherry"]
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")
#
# person = {"name": "John", "age": 30, "city": "New York"}
# for i,j in person.items():
#     print(f"{i}: {j}")

# for i in range(3):
#     for j in range(3):
#         print(f"i: {i}, j: {j}")
#
# names = ["Alice", "Bob", "Charlie", "David"]
# ages = [25, 30, 35]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")

# class MyIterable:
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         self.current = 0
#         return self
#
#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current - 1
#         else:
#             raise StopIteration
#
# for num in MyIterable(5):
#     print(num)
#
# l1=[1,2,3,4]
# l2=list(map(lambda x:x+5,l1))
# print(l2)

# str2=str(l1[1]+" "+l1[0])
# print(str2)str1="Hi Mirafra"
# l1=str1.split()
# str2=str(l1[1]+" "+l1[0])
# print(str2)
# def rev(str1):
#     l1=str1.split()
#     str2 = str(l1[1] + " " + l1[0])
#     return str2
# #
# print(rev(input("Enter a string: ")))

# str1='helola'
# l1=list(str1)
# l2=str1.split('l')
# print(l2)

# l=[9,1,8,9,3,6,8,5]
# for i in range(len(l)):
#     for j in range(0,len(l)-1-i):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(0, len(l) - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l
l = [9, 1, 8, 9, 3, 6, 8, 5]
print(bubble_sort(l))

# def selection_sort(l):
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#

