# import my_package
# print(my_package.greet())
# print(my_package.farewell())

# f=open("abhi.txt","w+")
# f.write("hello")
# f.close()
# a=open("abhi.txt","r")
# r=a.read()
# print(r)
# b=open("abhi.txt","w")
# for i in range(5):
#     b.write(str(i))
#     b.write("\n")
# b.close()
# a=open("abhi.txt","r")
# r=a.read()
# print(r)
# print(a.read(3))
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# w1=open("abhi.txt","w+")
# w1.writelines(L)
# a=open("abhi.txt","a")
# a.writelines("This is Texas")
# a.write("This is Berlin")
# l=['This is Madrid','This is Rome']
# a.writelines(l)
# a.close()
# r=open("abhi.txt","r")
# read=r.read()
# print(read)
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# f=open("abhi.txt","w")
# w=f.writelines(L)
# f.close()
# d={"cloth":['trending tshirt','branded tshirt','cotton tshirt','red tshirt'],
#  "toy":['Dr.set','kitchen setred', 'teddy','unicorn','fishing'],
#  "furniture":['chair','table','sofa']}
# f=open("abhi.txt","w")
# w=f.writelines("hgfjf")
# f.close()


# f=open("abhi.txt","x")
# s="aiusdhg"
# l=['j','k']
# len
# lst1=[0,0,1,1,1,2,2,3,3,3,4,4,4]
# lst2=[]
# for i in lst1:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

# # def num(lst1):
# lst1=[2,3,6,8,1,3,4]
# for i in range(len(lst1)):
#     for j in range(i+1,len(lst1)):
#         if lst1[j]<lst1[i]:
#             lst1[j],lst1[i]=lst1[i],lst1[j]
# print(lst1)
# for i in range(len(lst1)):
#     for j in range(len(lst1) - 1):
#         if lst1[j] > lst1[j + 1]:
#             lst1[j], lst1[j + 1] = lst1[j + 1], lst1[j]
# print(lst1)
lst1=[2,1,3,1,2,1]
lst2=[]
lst3=[]
temp=0
for i in range(0,len(lst1)):
    temp=lst1[i]
    for j in range (i+1,len(lst1)):
        if lst1[i]<lst1[j]:
            temp=lst1[j]
    lst2.append(temp)
print(lst2)


