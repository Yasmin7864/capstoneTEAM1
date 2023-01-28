'''def demo():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'

x=demo()
print(next(x))
print(next(x))'''


num=(x for x in range(10000))
print(num)
print(next(num))

n=[x*x for x in range(10000)]
print(n)


