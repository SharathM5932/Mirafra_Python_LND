def fibonacci():
    a,b = 0, 1
    while True:
        yield a
        a,b=b,a+b
fib=fibonacci()
for _ in range(10):
    print(next(fib))



def cal_sum():
    total=0
    while True:
        value=yield total
        if value is not None:
            total+=value
gen = cal_sum()
next(gen)
print(gen.send(10))
print(gen.send(5))
print(gen.send(3))
print(gen.send(None))