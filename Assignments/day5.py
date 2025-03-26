# #Generator
# def ten():
#     n=2
#     yield 1
#     yield 2
#     n+=10#n=12
#     print(n)
#     yield 3
#     a=121
#     print(a)
# for v in ten():print(v)#v=3
# print('done')

# def numberGenerator(n):
#     number = yield
#     #print(number)
#     while number < n:
#         number = yield number
#         #print(number)
#         number += 1
#
# g = numberGenerator(10)    # Create our generator
# g.send(None)
#
# print(g.send(5))
# print(g.send(6))
# print(g.send(5))

#send()
def ngen(n):#10
    num=yield#5 #so every time new value can be sent
    #only 1st time it will work (num=5)
    print('num1=',num)
    while num<n:#12
       # print('a=')
        num = yield num

         #=5 1st iter
        print('num2=',num)
        num+=1 #in 2nd iter
        print('num3=',num)
    else:yield
g=ngen(10)
next(g) #need in order to send value to generate
#just like iter and next... yield and next will let send to send the new new values every time
#print(g.send(None))
print(g.send(5)) #num values
print(g.send(2))
print(g.send(5))
print(g.send(11))


