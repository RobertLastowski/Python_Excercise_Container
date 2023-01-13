def fibbonacci():
    n1, n2 = 0,1
    while True:
        yield n1
        n1, n2 = n2, n1+n2

fib = fibbonacci()

for i in range(10):
    print(next(fib))