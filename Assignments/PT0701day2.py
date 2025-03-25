# def func(a=0,b,c):
#     print("hi")
# func(1,2,3)
# # def func(a=0,b,c):
# #                  ^
# # SyntaxError: parameter without a default follows parameter with a default
# #
'''
start=1
end=4
while start<=end:
    print(start)
    new_end=start+1
    while start<new_end:
        start+=0.1
        print(start%f,start)
    start=int(start)
    start+=1

'''
# s="hel lo"
# s1=list(s)
# print(s.split())
# print(s1)

# func to reverse the mirafra Hi
# s="Hi Mirafra"
# lst=s.split(' ')
# print(lst)
# s1=""
# for i in lst:
#     s1=i+" "+s1
# print(s1)

#
# s="Hi Mirafra"
# s1=""
# s2=""
# for i in s:
#     if i!=" ":
#         s1=s1+i
#         s3 = s1
#     elif i==" ":
#         s2=" "+s1
#         s1=""
# print(s3+s2)




# lst=[1,2,3,4]
# lst2=[i+5 for i in lst]
# print(lst2)

# lst1=
# lst2=
# if lst1>lst2:
#     print("lst1")
# else:
#     print("lst2")

# # Bubble sort
# def bubble_sort(arr):
#     for _ in range(len(arr)):
#         swap=True
#         for j in range(0,len(arr)-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 swap=False
#         if swap:
#             break
#     return arr
#
# arr=[37,25,277,1,2,45,10,35]
# print(bubble_sort(arr))

# arr=[1,2,3,1]
# arr.append(8,9)
# print(id(arr))
# arr1=arr.copy()
# print(id(arr1))

# arr1=[5,6]
# arr2=[9]
# arr.extend(arr1,arr2)
# print(arr.index(1,0,3))
# arr.insert(9)
# arr.pop(0)
# arr.remove(1)
# arr.reverse()
# print(arr)

# ==================================================
# STRING INBUILT
# ==================================================
# str1="anuroop"
# lst=[1,2,3]
# tup=(1,2,3)
# dict1={1:'an',2:'uroop'}

# n_row=int(input("n:"))
# matrix=[]
# m_col=int(input("m:"))
# for i in range(n_row):
#
#     lst = list(map(int, input("element:").strip().split()))[:m_col]
#     matrix.append(lst)
#
# print(matrix)




