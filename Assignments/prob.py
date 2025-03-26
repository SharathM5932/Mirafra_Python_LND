#o/p: [1,h,3,f,5,d,7,b]
a=[1,2,3,4,5,6,7,8,9,10]
b='abcdefghi'
l=[]
#1
b=list(b)
'''
c=a[::2]
k=b[-2::-2]
l=[]
for i in range(len(k)):
    l.append(c[i])
    l.append(k[i])

print(list(l))'''

#2
'''print(b)
j=[]
k=[]

for i in range(0,10,2):
    k.append(a[i])
for i in range(len(b)-1,-1,-1):
    if i%2!=0:
        j.append(b[i])

for i in range(0,len(j)):
    l.append(k[i])
    l.append(j[i])
print(l)

print(k,j)'''
#3
i,j=0,len(b)-2
while i < len(a) and j >= 0:
    if i % 2 == 0:
        l.append(a[i])
        #print(l)
    if j % 2 != 0:
        l.append(b[j])
        #print(l)
    i+=2
    j-=2
print(l)


