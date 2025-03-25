# Iterator
'''inf=iter(int,1)
print(next(inf))
print(next(inf))'''

'''class test:
    def __init__(self,a):
        self.a=a
    def __iter__(self):
        self.x=0
        return self
    def __next__(self):
        x=self.x
        if x<self.a:
            x+=1
            self.x=x
            return x
        else:
            exit()
for i in test(15):
    print(i)'''

# def ten():
#     print("h")
#     yield 1
#     print('a')
#     yield 2
# for i in ten():
#     print(i)

# decorator:changing functions behaviour
# example1:
'''def outer_func():
    print("outer")
    def inner_func():
        print("inner")
        return 2+8
    return inner_func()

print(outer_func())
print("done")'''

# example2
'''def add(n):return n+1
def sub(n):return n-1
print(add(3))
#
def cal(func):
    print(func(3))
cal(add)
cal(sub)'''

# example3:
'''def outer_func(func):
    def inner_func(a,b):
        a+b
    return inner_func
@outer_func
def add(a,b):
    print(a,b)'''

#example4:
#send()
def numberGenerator(n):
    number = yield
    #print(number)
    while number < n:
        number = yield number
        #print(number)
        number += 1

g = numberGenerator(10)    # Create our generator
# next(g)
g.send(None)

print(g.send(5))
print(g.send(6))
print(g.send(5))





# iterator
# generator
