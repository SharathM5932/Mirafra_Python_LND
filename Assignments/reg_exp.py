#1
import re
'''
s="rama, radha, krishna"
for i in re.finditer('radha',s):
    k=i.span()
    print(k)'''

#2
# print(re.split(r'a','an animal came to eat an apple'))
#
# #3
# list="lamb lamda","lotus lack","lion leather"
# for i in list:
#     b=re.match("(l\w+)\W(l\w+)",i)
#     if b:
#         print(b.groups())
#
# #4
# t='Python is an interpreted, high-level, general-purpose programming language'
# p='Python'
# print(re.search(p,t))
#
# #5
# text = "Do you use $ or ^ in regex?"
# escaped_text = re.escape(text)
# print("Escaped string:", escaped_text)
#
# #6
# text = "The rain in Spain falls mainly in the plain."
# res=re.subn(r'in','IN',text)
# print(res[0])
# print(res[1])

#7
# text = "apple, banana; grape, mango"
# result = re.split(r", |; ", text)
# print("After split:", result)

#8
text="apple, banana; grape, mango"
res=re.split(r", |; ",text)
print(res[0])
print(res[1])

#9
text = "Python is Fun!"
match = re.search(r"python", text, re.IGNORECASE)
if match:
    print("Found:", match.group())

#10
