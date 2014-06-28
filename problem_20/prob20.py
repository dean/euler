def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

print sum(map(int, list(str(factorial(100)))))
