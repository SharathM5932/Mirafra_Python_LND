
# 1
lst1=['Alice', 'Bob', 'Anna', 'Tom']
result=list(map(lambda x:x.upper(),filter(lambda x:x.startswith('A'),lst1)))
print(result)

# 2
import math
lst2=[-4, 9, 16, -1, 25]
result=list(map(lambda x:float(math.sqrt(x)),filter(lambda x:x>=0,lst2)))
print(result)

# 3
Words= ['apple', 'orange', 'pear', 'banana']
result=list(map(lambda x:x.upper(),filter(lambda x:'e' in x,Words)))
print(result)

# 4
lst4=[(1, 5), (3, 6), (4, 4), (2, 9)]
result=list(map(lambda x:x[0]*x[1],filter(lambda x:x[0]<x[1],lst4)))
print(result)

# 5
lst5=[2, 3, 2, 4, 5, 4]
result=list(map(lambda x:x**2 ,set(lst5)))
print(result)

# 6
result=list(map(lambda x:x/2,filter(lambda x:x%4==0,range(0,21))))
print(result)

# 7
result=list(map(lambda x:x**2,filter(lambda x:x%2!=0,range(0,10))))
print(result)

# 8
result=list(filter(lambda x:x%3==0 and x%5==0,range(1,50)))
print(result)

# 9
lst9=['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
result=list(filter(lambda x:x in "aeiou",lst9))
print(result)

# 10
words = ['apple', 'is', 'tasty', 'cherry', 'banana']
result=list(map(lambda x:len(x),filter(lambda x:len(x)>4,words)))
print(result)

# 11
lst11=['madam', 'hello', 'radar', 'world', 'level']
result=list(filter(lambda x:x==x[::-1],lst11))
print(result)

# 12
lst12=[1, 10, 100, 0, 1000]
result=list(map(lambda x:math.log(x,10),filter(lambda x:x>0,lst12)))
print(result)

# 13
result=list(filter(lambda x: all(x%i!=0 for i in range(2,int(x**0.5)+1)),range(2,49)))
print(result)