def fib(last, cur, end):
    while last+cur < end:
        yield last+cur
        last, cur = cur, last+cur
        

print sum((x for x in fib(0, 1, 4000000) if x % 2 == 0))
