# def fibo(num):
#     num1=0
#     num2=1
#     # print(num1)
#     # print(num2)
#     lst=[]
#     lst.append(num1)
#     lst.append(num2)
#     for _ in range(num-2):
#         num1,num2=num2,num1+num2
#         lst.append(num2)
#     return lst
#
# flag=True
# while flag:
#     try:
#         number=int(input("enter the number:"))
#         flag=False
#     except:
#         print("enter a integer")
#
# result=fibo(number)
# print(" ".join(map(str,result)))



# str1="Shikha is working in Wipro. She is from Jhanshi. Jhanshi is the automotive hub in India. Wipro is not having a office in Coimbatore"
# str2="Wipro is HQ in Bangalore and it works in different domains like Automotive, aerospace etc. Wipro may open a centre in Jhanshi soon"
# lst1=str1.split(" ")
# lst2=str2.split(" ")
# import re
# lst3=[]
# lst4=[]
# for i in range(len(lst1)):
#     if re.search(lst1[i],str2):
#         lst4.append(lst1[i])
#         continue
#     lst3.append(lst1[i])
# print("the common words:",lst4)
# print("common words removed in str1:"," ".join(map(str,lst3)))


import  re
# pattern=r'[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,4}'
# str1="test@example.com"
# if re.match(pattern,str1):
#     print("s")

# patt=r'\b(0[1-9]|[12][0-9]|[3][01])-(0[1-9]|1[0-2])-([0-9]{4})\b'
# str1="Today's date is 25-01-2025, tomorrow will be 26-01-2025."
# res=re.findall(patt,str1)
# print(res)

# pattern=r'\b\d{2}-\d{2}-\d{4}'
# str1="The event is scheduled on 23/01/2025, and the deadline is 15/02/2025."
# res=re.findall(pattern,str1)
# print(res)


# text = "This   is  a   sentence   with  extra spaces."
# str1=r'\s+'
# res=re.sub(str1," ",text)
# print(res)

# pattern=r'\b[Pp]\w*'
# str1="Python is Powerful and Popular"
# res=re.findall(pattern,str1)
# print(res)

# import re
#
# pattern=r'[0-1][0-9]|[2][0-3]:[0-5][0-9]'
# str1="23:59"
# if re.match(pattern,str1):
#     print("newu")

# print(os.listdir('G:\\My Drive\\Mirafra'))
# for i in os.listdir():
#     print(i)
# os.rename('anuroop.txt','anuroop111.txt')
# os.remove('anuroop111.txt')

import calendar
# print(calendar.month(2025,1))
# print(calendar.isleap(2024))

# for i in os.listdir():
#     st=os.stat(i)
#     print(i,st.st_ctime())

