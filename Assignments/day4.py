# dict1={i:i*i for i in range(1,11)}
# print(dict1)
# dict2={i:i*i for i in range(1,11) if i%2==0}
# print(dict2)

# fruits={'apple','banana','cherry'}
# dict3={i:len(i) for i in fruits}
# print(dict3)

# original={'a':1,'b':2,'c':3}
# dict4={j:i for i in original.keys() for j in original.values()   }
# print(dict4)

# keys=['name','age','gender']
# dict5={i:None for i in keys}
# print(dict5)

# numbers=range(1,11)
# dict6={i:('even' if i%2==0 else 'odd') for i in numbers}
# print(dict6)

# keys=['name','age','gender']
# values=['Alice',25,'Female']
# dict7={i:j for i in keys for j in values}
# print(dict7)

# nested ={'a':{'b':1,'c':2},'d':{'e':3,'f':4}}
# for i in nested:
#     for j in nested[i]:
#         print(i)
#         key=i+'_'+j
#         print(key)
#         print(nested[i][j])
# #
# dct={i+'_'+j:nested[i][j] for i in nested for j in nested[i]}
# print(dct)
'''3. #inputs:
l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]
# output-> lo=[6, 8, 1, 4, 8, 9, 2]
#l0=l1+l2 with carry'''

# print(9%2)
# l1=[4,5,6,7]
# l2=[2,3,5,6]
# lo=[]
# # sum=0
# carry=0
# for i in range(len(l1)):
#     if l2[i]+l1[i]<10:
#
#         sum=l2[i]+l1[i]
#
#         lo.append(sum)
#     else:
#         sum = l2[i] + l1[i]
#         carry=sum%10










