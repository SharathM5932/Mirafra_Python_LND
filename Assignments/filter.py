data ={'s1':['red','Silk',4500],'s2':['blood red','Silk',11500],
 's3':['pink','Silk',11200],'s4':['rose red','Party wear',6999],
 's5':['lemon yellow','Silk',8500],'s6':['brick red','Silk',8500],
 's7':['Green','Party wear',8999],'s8':['brick red','cotton',1500],
 's9':['Candy red','Silk',8500],'s10':['Ruby red','Silk',9999],}
print(data.values())
# l1=[i for i in data.values() if 'red' in i[0]]
# l1=[i for i in data.values() if 'red' in i[0] and i[2]<=10000 and i[1]=='Silk']
l1=list(filter(lambda i:data[i][1]=='Silk' and 'red' in data[i][0] and data[i][2]<=10000,data))
print(l1)