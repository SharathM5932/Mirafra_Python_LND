string = "A - 13, B - 14, C - 15"
# dict1={}
# lst=string.split(", ")
# print(lst)
# for val in lst:
#     dict1[val[0]]=val[4:]
# print(dict1)

# ----------------------------problem1------------------------

# dict1={val[0]:val[4:] for val in string.split(", ")}
# print(dict1)

# -----------------------------problem2-------------------------

# string = "11 - 13, 12 - 14, 13 - 15"
# dict1={int(val[:2]):int(val[4:]) for val in string.split(", ")}
# print(dict1)

# ------------------------------problem3------------------------
#
# n_row=int(input("n:"))
# matrix=[]
# m_col=int(input("m:"))
# for i in range(n_row):
#     lst = list(map(int, input("element:").strip().split()))[:m_col]
#     matrix.append(lst)
# print(matrix)

# -------------------------------PROBLEM4--------------------
import time
t=time.time()
l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]


print(t)
# output-> lo=[6, 8, 1, 4, 8, 9, 2]
l0=[]
i=0
carry=0
while i<len(l1) and i<len(l2):
    sum1=l1[i]+l2[i]+carry
    if sum1>=10:
        l0.append(sum1%10)
        carry=sum1//10
    else:
        l0.append(sum1)
        carry=0
    i+=1
while i<len(l1):
    sum1 = l1[i] + carry
    if sum1 >= 10:
        l0.append(sum1 % 10)
        carry = sum1 // 10
    else:
        l0.append(sum1)
        carry=0
    i+=1
while i<len(l2):
    sum1 = l2[i] + carry
    if sum1 >= 10:
        l0.append(sum1 % 10)
        carry = sum1 // 10
    else:
        l0.append(sum1)
        carry=0
    i+=1
print(time.time())
print(l0)

