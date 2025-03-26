# b=7
# a={b:1}
# print(type(a))
#dict keys are immutable,unordered collection,cannot sort list with diff data types
from operator import indexOf

a=[1,2,3,4,5,6,7,8,9,10]
b='abcdefghi'
l1=a[::2]
print(l1)
d=b[-2::-2]
print(d)
l2=[]
for i in d:
    l2.append(i)
print(l2)
op=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if i==j:
            op.append(l1[i])
            op.append(l2[j])

print(op)
# string = "A - 13, B - 14, C - 15"
# s=string.split(',')
# print(s)
# for i in range(len(s)):
#     s[i]=s[i].split('-')
# print(s)
# d1={i[0]:i[1] for i in s for j in i}
# print(d1)

# string = "11 - 13, 12 - 14, 13 - 15"
# s=string.split(',')
# print(s)
# for i in range(len(s)):
#   s[i]=s[i].split('-')
# print(s)
# d1={int(i[0]):int(i[1]) for i in s for j in i}
# print(d1)
#
# string = "A - 13, B - 14, C - 15"
# s=string.split(',')
# print(s)
# d1={i[0]:i[1] for i in [i.split('-') for i in s] for j in i}
# print(d1)

# string = "11 - 13, 12 - 14, 13 - 15"
# s=string.split(',')
# print(s)
# d1={int(i[0]):int(i[1]) for i in [i.split('-') for i in s] for j in i}
# print(d1)

# string = "A - 13, B - 14, C - 15"
# # s=string.split(', ')
# d1={i[0]:i[4:] for i in string.split(', ')}
# print(d1)

# row = int(input('Enter number of rows:'))
# column = int(input('Enter number of columns:'))
# matrix = []
# for i in range(row):
#     lst = []
#     for j in range(column):
#         data = input('enter value: ')
#         lst.append(data)
#     print(lst)
#     matrix.append(lst)
#
# print(matrix)


name = input('Enter your name:')
password = int(input('Enter the password:'))
person1 = bank_account(name, password)
data={"abhi":1234}

if name in list(data.keys()):
  if (name,password) in list(data.items()):
      print('yes')
  else:print('wrong password')
else:print('user name not found')

