"""for i in range(10):
    print(i)  """
"""fruits=['apple','orange','bluebeerry']
for fruit in fruits:
    print(fruit)  """

"""fruits=['apple','orange','bluebeerry']
for index,fruit in enumerate(fruits):
    print(f"index:{index} fruit:{fruit}")  """

"""person = {"name": "John", "age": 30, "city": "New York"}
for key,value in person.items():
    print(f"{key}:{value}")   """

"""for i in range(3):
    for j in range(3):
        print(f"i:{i} j:{j}")   """

"""sqaures=[i**2 for i in range(10)]
print(sqaures)"""

"""x=['alice','bob','charlie']
y=[23,34,56]
for i,j in zip(x,y):
    print(f"{i} is {j} years old")  """

"""for i in range(5):
    print(i)
else:
    print("loop finished without interruption")   """

"""from itertools import count
for i in count(10):
    print(i)
    if i > 15:
        break   """

"""x=[1,2,3,4,5]
y=[i+5 for i in x]
print(y)  """


"""a=2
b=2
print(id(a))
print(id(b))  """

x="Hi Mirafra"
"""a=x.split(" ")
print(a[1]+" "+a[0])  """

"""a=[]
for i in x.split(" "):
    a.append(i)
print(a[1]+" "+a[0])  """

"""a=['a',"b",1,2,3,[3,4],[5,6]]
b=[]
print(a)
print(b)
c=[i for i in range(0,10,2)]
print(c)
d=list(range(0,10,2))
print(d) """

"""a='hi,hello,well'
b=a.split(",")
print(b)  """

"""g="hello"
h=list(g)
print(h)  """

"""i=12345
j=[int(i) for i in str(i)]
print(j)  """

"""dict={"a":2,"b":4}
k=list(dict.keys())
print(k)
l=list(dict.values())
print(l)   """

m=[1,2,3,4]
"""n=[5,6,7,8]
m.append(9)
print(m)
m.extend(n)
print(m)"""

"""m.insert(2,5)
print(m)
print(m.index(3))
m.insert(3+2,"duck")
print(m)

m.remove('duck')
m.pop()
m.pop(1)
print(m)
m.clear()
print(m)     """

"""x=[1,4,7,3,9]
x.sort()
print(x)
print(sorted(x))  """

"""x=[4,3,5,2,1]
x[1:3]=[9]
print(x)  """

""" x=[9,56,733,40,1,33]
for i in range(len(x)-1,0,-1):
    for j in range(i):
        if x[j]>x[j+1]:
            swapped=True
            x[j],x[j+1]=x[j+1],x[j]
            print(x)
print(x)  """



"""a={1,3,5}
b={9,9,1}
print(a.symmetric_difference(b))
print(a^b) """

"""e={i:i*i for i in range(1,11)}
print(e)  """


"""s="A - 11,B - 12,C - 13"
dictionary = dict(i.split("-") for i in s.split(","))
print(dictionary)"""


"""s= "11 - 13, 12 - 14, 13 - 15"
a={int(i.split("-")[0]) : int(i.split("-")[1]) for i in s.split(",")}
print(a)"""

"""a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = 'abcdefghi'
d=b[-2::-2]
e=list(d)
z=[]
for i in a:
    if i%2!=0:
        z.append(i)
m=[]
for i in range(len(e)):
    m.append(z[i])
    m.append(e[i])
print(m)"""


"""x={i:i*i for i in range(101)}
print(x)"""

"""x=['apple','banana','cherry']
x={i:len(i) for i in x}
print(x)"""

"""x={'a':1,'b':2,'c':3}
x={j:i for i,j in dict.items(x)}
print(x)
"""
"""x=['name','age','gender']
x={i:'none' for i in x}
print(x)"""

"""numbers=range(1,11)
x={i:'Even' if i%2==0 else 'odd' for i in numbers }
print(x)"""

"""keys=['name','age','gender']
values=['alice',25,'female']
x={i:j for i,j in zip(keys,values) }
print(x)"""

"""x=['name','age','gender']
j='None'
x={i:j for i in x}
print(x)"""

x='hello world'
x={i:x.count(i) for i in x}
print(x)

x=range(65,91)
x={chr(i):i for i in x}
print(x)

"""x={'a':{'b':1,'c':2},'d':{'e':3,'f':4}}
x={k1+'_'+k2:k2.values() for k1,v1 in a.items() for k2,v2 in }"""


"""l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]
for i,j in zip(l1,l2):
    if i+j==10:"""

"""x=[1,2,3,4,5,6,7,8,9]
y='abcdefgh'
z=y[::-1]
a=[]
for i in x:
    if i%2!=0:
        a.append(i)
    print(i)"""

#Filter prime numbers in the range 0-49.
#x=[i for i in range(2,50) if(all(i%y!=0 for y in range(2,i)))]
#print(x)

#Filter palindromes from the list
"""x=['madam', 'hello', 'radar', 'world', 'level']
x=[i for i in x if i==i[::-1]]
print(x)"""

#Find the lengths of words longer than 4 characters in the list
"""x=['apple', 'is', 'tasty', 'cherry', 'banana']
y=map(len,filter(lambda i:len(i)>4,x))
print(list(y))"""

#Filter out vowels from the list
"""x=['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
y=filter(lambda i:i in ['a','i','e','o','u'],x)
print(list(y))"""

#Find all numbers in the range 1-50 that are divisible by both 3 and 5.
"""n=range(1,51)
x=filter(lambda i:i%3==0 and i%5==0,n)
print(list(x))"""

#For odd numbers in 0-9, calculate the sum of their squared digits.
"""numbers=range(0,10)
result = sum(map(lambda x: sum(int(digit)**2 for digit in str(x)), filter(lambda x: x % 2 != 0, numbers)))
print(result)"""

#Filter numbers divisible by 4 in the range 0-20 and divide them by 2
"""numbers=range(0,21)
result = list(map(lambda x: x / 2, filter(lambda x: x % 4 == 0, numbers)))
print(result)"""

#Remove duplicate numbers from [2, 3, 2, 4, 5, 4] and calculate their squares.
"""x=[2,3,2,4,5,4]
res=map(lambda i:i**2,set(x))
print(list(res))"""

#Filter words containing the letter 'e' and convert them to uppercase.
"""words=['apple', 'orange', 'pear', 'banana']
result = list(map(lambda word: word.upper(), filter(lambda word: 'e' in word, words)))
print(result)"""

#From the list of tuples [(1, 5), (3, 6), (4, 4), (2, 9)], filter tuples where the second element is greater than the first and compute their product.
#Output:[5, 18, 18]

#Calculate the base-10 logarithm of numbers greater than 0 in 
"""[1, 10, 100, 0, 1000].
Output:[0.0, 1.0, 2.0, 3.0]
"""