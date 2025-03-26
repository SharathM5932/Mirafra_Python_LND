
#------------------------------Matrix code--------------------------------------------

a=int(input('Enter the number of rows :'))
b=int(input('Enter the number of columns :'))
list=[]
print('Enter the Number:')
for i in range(a):
    list1=[]
    for j in range(b):
        list1.append(int(input()))
    list.append(list1)
print(list,end='\n\n')

for i in range(a):
    for j in range(b):
        print(list[i][j],end=' ')
    print()


#-----------------------------------code 1-------------------------------------------

string='A-13,B-14,C-15'
string=string.replace('-',',')
string=string.split(',')
dict={string[i]:string[i+1] for i in range(len(string))if i%2==0}
print(dict)

#--------------------------------code 2--------------------------------------------

string='11-13,12-14,13-15'
string=string.replace('-',',')
string=string.split(',')
dict={int(string[i]):int(string[i+1]) for i in range(len(string))if i%2==0}
print(dict)

# -------------------------------code 3----------------------------------------------

l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]
l3=[]
for i in range(len(l2)):
    if i<len(l1):
        if l1[i]+l2[i]>9:
            l2[i+1]=l2[i+1]+1
            l3.append(l1[i] + l2[i]-10)
        else:
            l3.append(l1[i]+l2[i])
    else:
        l3.append(l2[i])
print(l3)

