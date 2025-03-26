a=['Alice','Bob','Anna','Tom']
ansa=map(lambda x:x.upper(),filter(lambda x:x.startswith('A'),a))
print(list(ansa))

# -----------------------------------------------------
import math

b=[-4,9,16,-1,25]
ansb=map(lambda x:math.sqrt(x),filter(lambda x:x>0,b))
print(list(ansb))

#------------------------------------------------------
words=['apple','orange','pear','banana']
ans3=map(lambda x:x.upper(),filter(lambda x:'e' in x,words))
print(list(ans3))

#----------------------------------------------------------
lis=[(1,5),(3,6),(4,4),(2,9)]
ans4=map(lambda x:x[0]*x[1],filter(lambda x:x[0]<x[1],lis))
print(list(ans4))

#------------------------------------------------------------
a=[2, 3, 2, 4, 5, 4]
a=set(a)
ans5=map(lambda x:x*x,a)
print(list(ans5))

ans5=map(lambda x:x/2,filter(lambda x:x%4==0,range(0,21)))
print(list(ans5))
#------------------------------------------------------------
ans6=list(map(lambda x:x**2,filter(lambda x:x%2!=0,range(0,10))))
print(ans6)
#------------------------------------------------------------
ans7=list(filter(lambda x:x%3==0 and x%5==0,range(1,50)))
print(ans7)
#------------------------------------------------------------
li=['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
vo=['a', 'e', 'i', 'o', 'u']
ans8=list(filter(lambda x:x in vo,li))
print(ans8)

#------------------------------------------------------------
words = ['apple', 'is', 'tasty', 'cherry', 'banana']
ans9=list(map(lambda x:len(x),filter(lambda x:len(x)>4,words)))
print(ans9)
#------------------------------------------------------------
l=['madam', 'hello', 'radar', 'world', 'level']
ans10=list(filter(lambda x:x==x[::-1],l))
print(ans10)
#------------------------------------------------------------
import math
numbers = [1, 10, 100, 0, 1000]
ans11 = list(map(lambda x:math.log10(x),filter(lambda x:x >0,numbers)))
print(ans11)
#------------------------------------------------------------
ans12=list(filter(lambda n:n>1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)),range(50)))
print(ans12)