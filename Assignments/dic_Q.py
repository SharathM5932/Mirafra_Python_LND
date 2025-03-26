'''string = "A - 13, B - 14, C - 15"
k=string.split(", ")
j=[]
print(k)
'''
#1.1
'''for i in range(len(k)):
    #j.append(i.split(' - '))
    k[i]=k[i].split(' - ')
print(k)
res={i:j for i,j in k }
print(res)
res={s[:1]:s[4:] for s in k)
'''

#1.2
'''res={item.split(' - ')[0]: int(item.split(' - ')[1]) for item in k}
print(res)'''

#1.3
'''string=string.replace(' - ',' ').replace(', ',' ')
print(string)
j=string.split()
print(j)
res={j[i]:j[i+1] for i in range(0,len(j),2)}
print(res)'''

#2
'''str1="11 - 13, 12 - 14, 13 - 15"
str2=str1.split(', ')

res = {int(item.split(' - ')[0]): int(item.split(' - ')[1]) for item in str2}
print(res)
'''

#3
'''mat=[]
row=int(input("enter no of rows: "))
col=int(input("enter no of columns: "))
for i in range(row):
    row=[]
    for j in range(col):
        ele=int(input(f"enter elements: ({i},{j})"))
        row.append(ele)
    mat.append(row)
#for i in range(0,row):
print(mat)
for row in mat:
    print(row)
    '''

#4
'''fruits=['apple','banana','cherry']

res={i:len(i) for i in fruits}
print(res)'''

'''#4
keys=['name','age','gender']
res={i:None for i in keys}
print(res)'''

'''#5
num=range(1,11)
res={i:('even' if i%2==0 else 'odd') for i in num}
print(res)'''


'''keys=['name','age','gender']
values=['alice',25,'female']
res={key[i]:values[j] for i in len(keys) int(for j in len(values)}
print(res)'''

'''keys={chr(i):i for i in range(ord('A'),ord('Z')+1)}
print(keys)
'''


'''nest={'a':{'b':1,'c':2},'d':{'e':3,'f':4}}
#o/p:{a_b:1,a_c:2,d_e:3,d_f:4}
res={}
for out in nest:
    for inn in nest[out]:
        print(nest[out])
        print(inn)
        new_key=f'{out}_{inn}'
        print(new_key)
res={f'{out}_{inn}': nest[out][inn] for out in nest for inn in nest[out]}
print(res)'''

l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]
# output-> lo=[6, 8, 1, 4, 8, 9, 2]
#l0=l1+l2 with carry
c = 0
l=[]
for i in range(len(l1)):
    l0=l1[i]+l2[i]+c
    if l0<10:

        l.append(l0)
        c=0
    else:
        l.append(l0%10)
        c=l0//10
for i in range(len(l1), len(l2)):
    l0=l2[i]+c
    if l0<10:
        l.append(l0)
        c=0
    else:
        l.append(l0%10)
        c=l0//10
if c != 0:
    l.append(c)
print(l)



def d(a,b='hello'):
    print(f"{a},{b}")
d('manish')
d('bye!','manish')

