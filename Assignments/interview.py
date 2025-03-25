# to reverse a string without built in functions.
"""s="deepika"
rev=" "
for i in s:
    rev=i+rev
print(rev)"""

"""def factorial(n):
    if n<0:
        print("factorial is not possible for negative numbers")
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))"""


"""n=int(input("enter a number"))
if n>1:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("Not prime")"""


"""for i in range(2,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
"""
"""x=input("enter a string")
y=input("enter a string")
if sorted(x)==sorted(y):
    print("Anagram")
else:
    print("Not Anagram")"""


"""n=int(input("enter a number: "))
m=len(str(n))
s=0
temp=n
while temp>0:
    digit=temp%10
    s+=digit**m
    temp//=10
if n==s:
    print("Armstrong")
else:
    print("Not Amstrong")"""

# finding largest element from list.
"""x=[10,70,34,65]
max=x[0]
for i in x:
    if i>max:
        max=i
print(max)"""

# second largest element.
"""def find_second_largest(arr):
    if len(arr) < 2:
        return None  # There is no second largest element

    first = second = float('-inf')  # Initialize both variables to negative infinity

    for num in arr:
        if num > first:
            second = first  # Update second largest
            first = num  # Update largest
        elif num > second and num != first:
            second = num  # Update second largest

    if second == float('-inf'):
        return None  # If no second largest exists (i.e., all elements are the same)

    return second


# Example usage
arr = [12, 35, 1, 10, 34, 1]
print(find_second_largest(arr))  # Output: 34
"""




#palindrome.
"""def check_palindrome(n):
    y=" ".join(reversed(n))
    if n==y:
        print("palindrome")
    else:
        print('no')

check_palindrome("racecar")"""

"""
x=[2,6,1,8]
s=0
for i in x:
    s+=i
print(s)"""

"""s="this is first string"
n="this is second string"
s1=set(s.split(" "))
n1=set(n.split(" "))
uncommon_words=s1.symmetric_difference(n1)
print(list(uncommon_words))"""

"""s="this is first string"
n="this is second string"
s1=set(s.split(" "))
n1=set(n.split(" "))
common_words=s1.intersection(n1)
print(list(common_words))"""

"""s="This is a test test string string"
word=set(s.split(" "))
duplicates=" ".join(word)
print(duplicates)"""

"""s="This is a test test string string"
n="This is a mac mac is string"
w1=set(s.split(" "))
n1=set(n.split(" "))
dupliactes=w1.intersection(n1)
print(dupliactes)
print(w1)"""


"""s="priyadarshini"
m=""
for i in s:
    if i not in m:
        m+=i
print(m)"""

def rec_fibonacci_series(n):
    if n <= 0:
        return []  # If n is 0 or negative, return an empty list
    elif n == 1:
        return [0]  # Only the first Fibonacci number
    elif n == 2:
        return [0, 1]  # The first two Fibonacci numbers

    # Recursively calculate the Fibonacci series up to n
    series = rec_fibonacci_series(n - 1)
    series.append(series[-1] + series[-2])  # Append the next Fibonacci number
    return series

# Example usage
print(rec_fibonacci_series(10))



"""def rec_fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    s=rec_fibonacci(n-1)
    s.append(rec_fibonacci(-1)+rec_fibonacci(-2))
    return s
rec_fibonacci(10)"""


"""def missing_numbers(x):
    n=len(x)+1
    s=n*(n+1)//2
    return s-sum(x)
print(missing_numbers([1,2,3,5]))"""

"""def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped=True


arr=[39,12,18,85,72,10,2]
print(arr)
bubble_sort(arr)
print(arr)"""


"""def first_non_repeating_char(s):
    for char in s:
        if s.count(char)>1:
            return char
    return None
print(first_non_repeating_char('deepika'))"""


"""def intersection_lists(list1,list2):
    return list(set(list1) & set(list2))
print(intersection_lists([8,6,5,9],[8,4,6,1]))"""

# def difference(list1,list2):
#     return list(set(list1) - set(list2))
# print(difference([7,4,8,2],[6,9,3,2]))


# def largest_sum(list):
#     list.sort()
#     return list[-1]+list[-2]
# print(largest_sum([7,3,98,54,123]))


"""def frequency_element(s):
    freq={ }
    for i in s:
        freq[i]=s.count(i)
    print(freq)
frequency_element([1, 2, 2, 3, 3, 3, 4])"""


"""def find_missing_numbers(s):
    n=len(s)+1
    total=n*(n+1)//2
    return total-sum(s)
print(find_missing_numbers([1,2,3,5]))



def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left < right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif left<arr[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
arr=[1,5,8,9,10]
print(arr)
print(binary_search(arr,9))"""


"""def remove_duplicates(n):
    x=[]
    for i in n:
        if i not in x:
            x.append(i)
    print(x)
remove_duplicates([10,20,20,70,18])"""

"""n=int(input("enter a value"))
if n>1:
    for i in range(2,(n+1)//2):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("prime")
else:
    print("Not prime")"""


#find duplicates
"""def duplicates(x):
    dupli=set()
    seen=set()
    for i in x:
        if i in seen:
            dupli.add(i)
        else:
            seen.add(i)
    return list(dupli)
print(duplicates([1,2,2,1,3,4,1,5]))"""


"""def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
fibonacci(10)"""

"""def duplicates(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    print(y)
duplicates([1,2,2,4,4,5,6])"""


import re
# string="This year is beautiful"
# x=re.findall(r'\w+',string)
# print(x)
#
#
# pattern=r'\b[a-zA-Z0-9-+.%]+@[a-zA-Z0-9.-]+\.[a-z|A-Z]{2,7}\b'
# m=re.findall(pattern,'contact us at support@gmail.com')
# print(m)

# x=re.findall(r'\b\d{3}[_.]?\d{3}[-.]?\d{4}\b','my phone number is 123-456-7890 or 123.456.7890.')
# print(x)
#
# a=re.findall(r'\b[A-Z][a-z]*\b','Alice and Bob both are friends.')
# print(a)
#
# m=re.findall(r'\W+','This year is 2025!')
# print(m)
#
# u=re.findall(r'(\w+)@(\w+)\.(\w+)','deepika.chowdary246@gmail.com')
# print(u)
#
# i=re.findall(r'\b\d{2}[-/]\d{2}[/-]\d{4}\b',"dates are 12-03-2025 and 25/03/2025")
# print(i)

# pattern=r'[+-]?[0-9]*\.?[0-9]+'
# x=re.findall(pattern," temperatures: 1,3.98,-3.14,8.9,5")
# print(x)
#
#
# string="This is a test test to find repeated repeated words."
# pat=r'\b(\w+)\s+\1\b'
# v=re.findall(pat,string)
# print(v)
#
# s=re.sub(r'\s+'," ","the    test   is  completed")
# print(s)
#
# c=re.findall(r'#(\w+)',"#python is a #language")
# print(c)



string="Today's date is 2025-03-11"
x=re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',string)
print(x.group())