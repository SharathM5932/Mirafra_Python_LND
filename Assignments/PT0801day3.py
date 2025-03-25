# dictionary=========
# key are immutable.
# can not have 2 more value separated with comma
# set does not support indexing
# while creating if there are 2 or more similar keys then the first will be replaced by the 2 element
# dict1={2:1,2:3}
# print(dict1)

# list with different datatype can not be sorted
# can not sort dictionary
# c=['biriyani','gobi']
# print(':'.join(map(str,c)))

#
a=[1,2,3,4,5,6,7,8,9,10]
b='abcdefghi'
# lst=[]
# for i in range(0,len(a),2):
#     lst.append(a[i])
c=b[::-1]
# for i in range(1,len(b),2):
#     lst.insert(i,c[i])
# print(lst)

# dict1={}
# lst=[]
# for i in range(0,len(a)-2,2):
#     dict1[a[i]]=c[i+1]
#
# for key,value in dict1.items():
#     lst.append(key)
#     lst.append(value)
# print(lst)

# for i in range(1,len(a)-2,2):
#     a[i]=b[len(b)-1-i]
# print(a[:len(b)-1])

# wrapping -
# transpose matrix
# matrix=[[1,2,3,4],[5,6,7,8]]
# new_matrix=[]
# for i in range(len(matrix[0])):
#     new_lst=[]
#     for row in matrix:
#         new_lst.append(row[i])
#     new_matrix.append(new_lst)
# print(new_matrix)

# frozen set -

# a={2,3}
# b={1,4}
# # b=frozenset(a)
# #
# # a.add(7)
# # print(a)
# # print(b)
# print("union",a.union(b))
# a.intersection(b)
#
# row=int

# a=float(input())
# a+=2
# print(a)

# amount=1234
# str1=str(amount)
# print('x'*(len(str1)-2)+str1[len(str1)-2:])




