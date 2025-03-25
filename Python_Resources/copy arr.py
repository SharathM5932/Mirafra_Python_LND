from array import *
import numpy as np
#operations on array
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
"""c=a+b
print(c)
print(np.sin(a))
print(np.log(a))
print(min(a))
print(np.concatenate([a,b]))
# copying an array
#Shallow copy
"""c=a
print(c)
print(id(a))
print(id(c))
c=a.view()
print(id(a))
print(id(c))
a[2]=0
print(c)"""
#Deep copy
c=a.copy()
a[2]=1
print(a)
print(c)



