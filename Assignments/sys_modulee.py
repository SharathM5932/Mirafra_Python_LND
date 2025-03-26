import sys
#1
# def print_stderr(*a):
#     print(*a,file=sys.stderr)
# print_stderr("hello")

#2
# age=17
# if age<18:
#     sys.exit("Age less than 18")
# else:
#     print("Age is not less than 18")
# print('bye')

#3
# print(sys.modules)

#4
#sys.getrefcount() method is used to get the reference count for any given object. This value is used by Python as when this value becomes 0, the memory for that particular value is deleted.
# a = 5
# print(sys.getrefcount(a))
#or a='deepthi' or a sentances

#5
print(sys.version)
print(sys.argv)

#6



