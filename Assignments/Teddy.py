s=input('Enter the name of products stored in the cotton box:')
out=[]
c=0
st=s.split(',')
for i in st:
    if 'teddy' in i:
        c+=1
        out+=[i]
print('Dear Surya')
print('Total',c,'teddies are there. And, here they are:')
print(out)
