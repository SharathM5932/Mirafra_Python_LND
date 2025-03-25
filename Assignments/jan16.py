"""from abc import ABC
class Car(ABC):
    def mileage(self):
        pass
class Tata(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Honda(Car):
    def mileage(self):
        print("The mileage is 20kmph")
class Mg(Car):
    def mileage(self):
        print("The mileage is 25kmph")
class Duster(Car):
    def mileage(self):
        print("The mileage is 19kmph")"""
"""t=Tata()
t.mileage()
h=Honda()
h.mileage()
m=Mg()
m.mileage()
d=Duster()
d.mileage()"""

"""for i in Tata(),Honda(),Duster(),Mg():
    i.mileage()"""

"""from abc import ABC
class R(ABC):
    def rk(self):
        print("hello")
class K(R):
    def k(self):
        super().rk()
        print("bye")"""

"""class bill:
    def __init__(self, m, u):
        self.m = m
        self.u = u

    def __add__(self, other):
        m = self.m + other.m
        u = self.u + other.u
        bill1 = bill(m, u)
        return bill1
    def __gt__(self, other):
        a=(self.m +other.m)>(self.u+other.u)
        return a


a1 = bill(5000, 15000)
a2 = bill(25000, 5000)
a = a1 > a2

if a == True:
    print("My bill is greater")
else:
    print("Your bill is greater")
a, b, c = 2, 3, 'Animesh'
print(a + b)
print(str(a) + c)"""


def add(x,y):
    return x+y
def self(x,y,z):
    return x+y+z

print(add(2,3))
print(self(5,6,7))
