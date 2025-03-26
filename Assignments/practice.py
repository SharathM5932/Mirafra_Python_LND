# s='123'
# l=[]
# for i in range (len(s)):
#     for j in range (i+1,len(s)+1):
#         l.append(s[i:j])
# print(l)
#
# for i in l:
#     if i==i[::-1] and len(i)>1:
#         print(i)
from pyflakes.checker import counter

# num=1212
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

s='swiss'

# d={}
# for i in range(len(s)):
#     count = 1
#     for j in range(i+1,len(s)):
#         if s[i]==s[j]:
#             count+=1
#     if count==1:
#         print(s[i])
#         break
# c=counter(s)
# for i in c.keys():
#     if c[i]==1:
#         print(i)
#         break
# print(c)

# a="abca"
# b="caba"
# for i in b:
#     if i not in a:
#         print("no anagram")
# else:
#     print("anagram")
# a="aabbbccdabcd"
# d={}
# for i in range(len(a)):
#     count=1
#     if a[i] not in d:
#         for j in range(i+1,len(a)):
#             if a[i]==a[j]:
#                 count+=1
#
#         d[a[i]]=count
# print(d)

def freq(string):
    d={}
    for i in range(len(string)):
        count = 1
        if string[i] not in d:
            for j in range(i + 1, len(string)):
                if string[i] == string[j]:
                    count += 1

            d[string[i]] = count
    return d
# d1=freq("abhia")
# d2=freq("iahba")
# if d1==d2:
#     print("anagram")
# else:print("not a anagram")

#first non repeating element in a string
d3=freq("swiss")
print(d3)
for i in d3.keys():
    if d3[i]==1:
        print(i)
        break
