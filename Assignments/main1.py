'''from module_pack.add import N_add2,N_add3,str_add
from module_pack.multiply import mul
N=N_add3(1,4,5)
k=N_add2(5,99)
s=str_add('man','ish')
m=mul(4,55)
print(N,k,s,m)'''

'''import dir_init_ex as d

#main.py

print(d.greet())      # Output: Hello from module1!
print(d.farewell())   # Output: Goodbye from module2!'''

#main.py
from dir_init_ex import *
print(greet())      # Output: Hello from module1!
print(farewell())  # Raises NameError: name 'farewell' is not defined