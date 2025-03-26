#1
import math
print(math.ceil(-32.1))
print(math.ceil(5.1))
print(math.ceil(5.9))
c=7
print(c.__ceil__())

#2
#floor() method in Python returns the floor of x i.e., the smallest integer not lesser than x.
import math
print(math.floor(7))
print(math.floor(7.9))
print(math.floor(7.1))
print(math.floor(-0.5))#=-1
c=444
print(c.__floor__())

#3
#copysign
math.copysign(3.4,0.0)
math.copysign(3.4,-7.8)
print(math.copysign(-3.4,-7.8))

#4
print(math.factorial(5))

#absolute value
print(math.fabs(-8.9))

#5
#nan-not a number
# math.isnan(5)
# math.isnan('geeta')#-> error

#6
print(math.lcm(3,13),math.gcd(3,13))

#7
a=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
print(math.fsum(a))
# 0.8
print(sum(a))
# 0.7999999999999999

#8
# round(1.5),7.5,11,5 is the next whole no.
# But round(10.5), 20.5,30.5 is the previouus no. i.e. 10,20,30

