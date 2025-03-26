# 1. Write a generator function that produces the Fibonacci sequence indefinitely. Use yield to return the next number in the sequence.
#
# 2. Write a generator that calculates the running sum of numbers sent to it using send. If None is sent, it should return the current total.
#
# 3. Implement a class-based iterator to generate the first n prime numbers.

#1
def fib(n):
    a,b=0,1
    for _ in range(n):
        yield a
        a,b=b,a+b
fibb=fib(10)
for i in fibb:
    print(i)

#2
