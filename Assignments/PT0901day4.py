# l1=[4,5,6,7]
# l2=[2,3,5,6,7,9,2]
# l0=[]

# ---------------assignment2dict---------------------------
# dict1={i:i**2 for i in range(1,11)}
# print(dict1)
#
# dict1={i:i**2 for i in range(2,11)}
# print(dict1)
# # dict1
# dict1={'a':1,'b':2,'c':3}
# dict2={val:key for key,val in dict1.items()}
# print(dict2)
#
# #5
# keys=['name','age','gender']
# dict5={x:None for x in keys}
# print(dict5)
#
# numbers=range(1,11)
# dict6={i:'odd' if i%2  else 'even' for i in range(1,11)  }
# print(dict6)
#
# keys=['name','age','gender']
# values=['alice',25,'female']
# dict7={keys[i]:values[i] for i in range(len(keys))}
# print(dict7)
#
#
# dict8={chr(i):i for i in range(65,91)}
# print(dict8)
#
# nested={'a':{'b':1,'c':2},'d':{"e":3,'f':4}}
# for x in nested.items():

"""str1="hello world"
dict10={}
for i in str1:
    if i not in dict10:
        dict10[i]=1
    else:
        dict10[i]+=1
print(dict10)

dict10={i:str1.count(i) for i in str1}
print(dict10)"""




#
# ------------------------------------------------------------
# def dee(a:int,b:int): #even will declaring that the data type is int still it executes
#     return 'hi'       #because we are not using them
# print(dee(1,2))
# print(dee('1',2))

# ---------------Recursion------------
# if no end point gives recursion error

# # -----------------
# add=lambda a,b:a+b
# print(add(2,3))

def fun(a,b):print(a+b)
def fun(a,b):print(a-b)

fun(2,3)



