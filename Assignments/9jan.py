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