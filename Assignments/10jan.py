"""l=[1,3,4,5,7]
#for i in a:print(i)
a=iter(l)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))"""

"""class Test:
    def __init__(self, a):self.a= a
    def __iter__(self):
        self.x = 10
        return self
    def __next__(self):
        x = self.x
        if x > self.a:
            raise StopIteration
        self.x = x + 1
        return x

for i in Test(15):
    print(i)"""

"""l={1,3,4,8,5}
m={9,2,3,92,1}
a=iter(l.intersection(m))
print(a)
print(next(a))
print(next(a))"""

"""int()
inf=iter(int,1)
print(next(inf))
print(next(inf))"""


"""inf=iter([i for i in range(3)])
print(next(inf))
print(next(inf))
print(next(inf))"""

"""inf=iter({i:i**2 for i in range(10) if i%2==0})
print(next(inf))
print(next(inf))
print(next(inf))"""


"""x=iter([i.upper() for i in ['apple','banana','cherry']])
print(next(x))
print(next(x))
print(next(x))"""


"""def ten():
    n=1
    while n<=10:
        sq=n*n#9
        yield sq
        n+=1
value=ten()#1,4,9
print(value)
for i in value:print(i)"""

