"""functions (findall,search pattern,match,split,sub)"""
#regex is a special sequence of characters that uses a search pattern ton find a string or set of string
import re
# a="welcome to python this is python"
# b=re.match("we",a)
# print(b)
# c=re.match("py",a)#py is not present at first so returns none
# print(c)
# d=re.search("py",a)#even py present twice it shows only once
# print(d)
# print(type(d))
# e=re.findall("py",a)#returns a list and how many times py present that many elements returns
# print(e)
# f=re.findall("ab",a)#retuns empty list
# print(f)
# g=re.split("python",a)
# print(g)
# h=re.sub("python","java",a)
# print(h)
# print(type(h))
# i=re.sub("python","java",h)
# print(i)
a="my name is abhishek , my age is 23"
# b=re.findall("\Amy",a)#\A checks whether string string start with my
# print(b)
# b=re.findall("\Aname",a)#string not start with name and returns empty list
# print(b)
# b=re.findall("23\Z",a)
# # print(b)
# b=re.findall("is\Z",a)
# print(b)
# b=re.findall("\s",a)#count all spaces
# print(b)
# b=re.findall("\S",a)#counts everything except spaces
# print(b)
# b=re.findall("\d",a)
# print(b)
# b=re.findall("\D",a)
# print(b)
# b=re.findall("\w",a)
# print(b)
# b=re.findall("\W",a)
# print(b)
# b=re.findall(r"\ba",a)
# print(b)
# b=re.findall(r"ek\b",a)
# print(b)
# b=re.findall(r"\Bek",a)
# print(b)
# b=re.search(r"\Bek",a)
# print(b)
# a="my name is abhishek , my age is 23"
# b=re.findall("^my",a)#starts with
# print(b)
# b=re.findall("^is",a)
# print(b)
# b=re.findall("23$",a)#ends with
# print(b)
# b=re.findall("ek$",a)
# print(b)
# b=re.findall("a.e",a)
# print(b)
# b=re.findall("a...s",a)
# print(b)
# b=re.findall("my|is",a)
# print(b)
# b=re.findall("abhishek|abc",a)
# print(b)
# a="my name is ABHISHEK , my age is 23"
# b=re.findall("[a-z]",a)
# print(b)
# b=re.findall("[0-9]",a)
# print(b)
# b=re.findall("[A-Z]",a)
# print(b)
# b=re.findall("[^A-Z]",a)
# print(b)
# a="my name is abhishek"
# b=re.findall(r"\bab\w+ek\b",a)
# print(b)
x="abhi_ag@gm1il.com"
# [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
b=re.findall(r"[\b\w]+\@[\w]+[\w+$]",x)
print(b)
