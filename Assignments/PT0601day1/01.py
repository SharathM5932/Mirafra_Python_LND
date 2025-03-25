# res = 5+55+555
# print(res)

def func(n):
    res = []
    for i in range(1, 4):
        res.append(str(n) * i)
    # print(res)

    res_list = list(map(int, res))
    print(sum(res_list))

def anuroop(a,b):
    return a+b


# ip = int(input('Enter the number: '))
# func(ip)