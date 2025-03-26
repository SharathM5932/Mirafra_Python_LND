import math
'''
k=['Alice', 'Bob', 'Anna', 'Tom']
#Output:['ALICE', 'ANNA']
def first(n):
    for i in k:
        if i[0]=='A':
            return i
    return
l=filter(first(k),k)
print(l)'''

#1
'''res=[i.upper() for i in filter(lambda i:i[0]=='A',k)]
print(res)'''


#2
'''a=[-4, 9, 16, -1, 25]
a1=[]
for i in a:
    if i>0:
        a1.append(i)
print(a1)

#Output:[3.0, 4.0, 5.0]
res=list(map(lambda x:math.sqrt(x),a1))
print(res)'''

'''#3
#Filter words containing the letter 'e' and convert them to uppercase.
words=['apple', 'orange', 'pear', 'banana']
#Output:['APPLE', 'ORANGE', 'PEAR']

res=[i.upper() for i in filter(lambda i:'e' in i,words)  ]
print(res)'''

'''#4
#From the list of tuples [(1, 5), (3, 6), (4, 4), (2, 9)], filter tuples where the second element is greater than the first and compute their product.
#Output:[5, 18, 18]
k=[(1, 5), (3, 6), (4, 4), (2, 9)]
l2=[]
for i in k:
    if i[0]<i[1]:
        print(i[1])
        l2.append(i[1]*i[0])
print(l2)

l2=list(map(lambda i:i[1]*i[0],filter(lambda i:i[0]<i[1],k)))
print(l2)'''


'''#5
#Remove duplicate numbers from [2, 3, 2, 4, 5, 4] and calculate their squares.
#Output: [4, 9, 16, 25]
k=[2, 3, 2, 4, 5, 4]
l2=[]
k=set(k)
print(k)
for i in k:
    l2.append(i**2)
print(l2)

l2=list(map(lambda x:x**2 ,set(k) ))
print(l2)

l2=[i**2 for i in set(k)]
print(l2)'''

'''#6
#Filter numbers divisible by 4 in the range 0-20 and divide them by 2.
#Output:[0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
k=[i for i in range(0,20+1)]
l2=[]
for i in k:
    if i%4==0:
        l2.append(i/2)
print(l2)

l2=[x/2 for x in filter(lambda x:x%4==0,k)]
print(l2)
'''

'''#7
#For odd numbers in 0-9, calculate the sum of their squared digits.
#Output:[1, 9, 25, 49, 81]
k=[i for i in range(0,9+1)]
l2=list(map(lambda x:x**2 ,filter(lambda x:x%2!=0,k)))
print(l2)
'''

'''#8
#Find all numbers in the range 1-50 that are divisible by both 3 and 5.
#Output: [15, 30, 45]
k=[i for i in range(1,50+1)]

l2=list(filter(lambda x:x%3==0 and x%5==0,k))
print(l2)'''

'''#9
#Filter out vowels from the list
#['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z'].
#Output:['a', 'e', 'i', 'o', 'u']
v=['a', 'e', 'i', 'o', 'u']
k=['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
l2=list(filter(lambda x:x in v,k))
print(l2)'''

'''#10
#Find the lengths of words longer than 4 characters in the list
#['apple', 'is', 'tasty', 'cherry', 'banana'].
#output: [5, 5, 6]
words = ['apple', 'is', 'tasty', 'cherry', 'banana']
l2=list(map(len,filter(lambda x:len(x) > 4,words)))
print(l2)
'''

'''#11 Filter palindromes from the list ['madam', 'hello', 'radar', 'world', 'level'].
#Output:['madam', 'radar', 'level']
k=['madam', 'hello', 'radar', 'world', 'level']
l2=list(filter(lambda x:x==x[::-1],k))
print(l2)'''

'''#12
#Calculate the base-10 logarithm of numbers greater than 0 in
k=[1, 10, 100, 0, 1000]
#Output:[0.0, 1.0, 2.0, 3.0]
l2=list(map(lambda x:math.log10(x),filter(lambda x:x>0,k)))
print(l2)'''

'''#13
#Filter prime numbers in the range 0-49.
#Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

k=[i for i in range(0,49)]
l2=[]
print(k)
for x in range(2,len(k)):
    prime=True

    for i in range(2,k[x]):
        if k[x] % i == 0:
            prime = False
            break
    if prime:
        l2.append((k[x]))
        
        
res=list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x>1 , k))
print(res)'''

