'''l1=[int(x) for x in input().split()]
print(l1)
m=list(map(lambda x:x+5,l1))
print(m)'''

def rev(str1):
    if " " not in str1:
        x=list(str1)
        str2 = ''.join(x[::-1])
    else:
        x=str1.split()
        str2 = str(x[1] + ' ' + x[0])

    return str2

a=rev(input("enter string: "))
print(a)