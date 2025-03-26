'''
#function secur_nested
def outside(a):
    def inside():
        return a()+1
    return inside
def onemore():
    return 6
haha=outside(onemore)
print(haha())'''

#1
