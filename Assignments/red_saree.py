input_saree=(input("Enter the product details to store it into our data base:"))
input_saree=eval(input_saree)
red=[]
for i in input_saree:
    if 'red'in input_saree[i][0]:
        if 'Silk'in input_saree[i][1]:
            if input_saree[i][2]<10000:
              red.append(i)
    else:
        pass
print(red)
#or

sarees=list(filter(lambda n:'red' in input_saree[n][0] and input_saree[n][1]=='Silk' and input_saree[n][2]<=10000 ,input_saree))
print(sarees)
#l1=list(filter(lambda i:'red' i in input_saree[i][0]  ))

"""d1={'s1':['red','Silk',4500],
    's2':['blood red','Silk',11500],
    's3':['pink','Silk',11200],
    's4':['rose red','Party wear',6999],
    's5':['lemon yellow','Silk',8500],
    's6':['brick red','Silk',8500],
    's7':['Green','Party wear',8999],
    's8':['brick red','cotton',1500],'s9':['Candy red','Silk',8500],'s10':['Ruby red','Silk',9999],}

"""