# #anagram
# k = "below"
#
# input1 = input("enter: ")
# for i in range(len(k)):
#     match = False
#     for j in range(len(input1)):
#         if k[i] == input1[j]:
#             match = True
#             break
#         else:
#             match = False
#     if not match:
#         break
#
# if match == True and len(k) == len(input1):
#     print("anagram")
# else:
#     print("no")


# #Find the First Non-Repeating Character. input="swiss"
# k='lsannabal'
# n=len(k)
# i=0
# while i<len(k):
#     count = 0
#     j = len(k) - 1
#     while j>=0:
#         if k[i]==k[j]:
#             count+=1
#         j-=1
#     if count==1:
#         print(k[i])
#         break
#     i+=1


#

k= '123'
m=[[]]
for i in k:
    new=[]
    for j in m:
        new.append((j+[i]))
    m+=new
print(m)





