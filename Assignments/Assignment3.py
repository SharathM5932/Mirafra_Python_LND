

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(10):
    print(next(fib))

# ==========================================
def running_sum():
    total = 0
    while True:
        num = yield total
        if num is not None:
            total += num

sum_gen = running_sum()
print(next(sum_gen))  # Initialize
print(sum_gen.send(5))  # Add 5
print(sum_gen.send(3))  # Add 3
print(sum_gen.send(None))

# ======================================

class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.num = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            while not self.is_prime(self.num):
                self.num += 1
            prime = self.num
            self.num += 1
            self.count += 1
            return prime
        else:
            raise StopIteration

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


prime_iter = PrimeIterator(10)
for prime in prime_iter:
    print(prime)