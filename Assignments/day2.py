n=1
while n<=5:
    print(n)
    i=0
    while True:
        i+=1
        print(f"{n}.{i}")
        if i==9:
            break

    n+=1

#o/p: [('gfg',300),('is',30),('best',150)]
t=[('gfg',50),('gfg',50),('is',30),('best',100),
   ('gfg',200),('best',50)]
