#.Write a generator function that produces the Fibonacci sequence indefinitely.
# Use yield to return the next number in the sequence.
"""def fib_num(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        yield a
x=fib_num(10)
print(x)
for i in fib_num(10):
    print(i)"""


"""def sum():
    total=0
    while True:
        n=yield total
        if n is not None:
            total+=n
        else:
            yield total

g=sum()
next(g)
print(g.send(1))
print(g.send(2))
print(g.send(3))
print(g.send(None))"""


class PrimeIterator:
    def _init_(self, n):
        self.n = n
        self.count = 0
        self.current = 2

    def _iter_(self):
        return self

    def _next_(self):
        while self.count < self.n:
            if self.is_prime(self.current):
                self.count += 1
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


# Example usage:
n = 10  # The number of primes to generate
prime_iterator = PrimeIterator(n)

for prime in prime_iterator:
    print(prime)