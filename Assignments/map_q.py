
# l=['Alice', 'Bob', 'Anna', 'Tom']
# def cap(l):
#     for i in l:
#         if i[0]=='A':
#             a=i.upper()
#             return a
# print(cap(l))
#
# l1=list(map(lambda x:x.upper(),filter(lambda name:name.startswith('A'),l)))
# print(l1)

# import math
# l=[-4, 9, 16, -1, 25]
# l1=list(map(lambda x:math.sqrt(x),filter (lambda x:x>0,l)))
# print(l1)

# l=['apple', 'orange', 'pear', 'banana']
# l1=list(map(lambda x:x.upper(),filter(lambda x:x.endswith('e'),l)))
# print(l1)
#
# a=list(map(lambda x:x[0]*x[1],filter(lambda x:x[0]<x[1],l)))
# print(a)
# l=[2, 3, 2, 4, 5, 4]
# a=list(map(lambda x:x*x,set(l)))
# print(a)

# a=[i for i in range (1,21)]
# print(a)
# l=list(map( lambda x:x/2,filter(lambda x:x%4==0,[i for i in range (1,21)])))
# print(l)

# l=list(map( lambda x: x**2,filter(lambda x:x%2!=0,[i for i in range(1,11)] )))
# print(l)

# l=list(filter(lambda x: x%3==0 | x%5==0,[i for i in range(1,51)]))
# print(l)

# l=['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
# o=['a','e','i','o','u']
# l1=list(filter(lambda x:x in o,l))
# print(l1)

# l=['apple', 'is', 'tasty', 'cherry', 'banana']
# l1=list(map(lambda x:len(x),filter(lambda x:len(x)>4,l)))
# print(l1)

l=['madam', 'hello', 'radar', 'world', 'level']
l=list(filter(lambda x : x==x[::-1],l))
print(l)