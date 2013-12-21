from math import sqrt

# Inefficient, but should solve within 2 mins.
def is_prime(n):
    for x in range(2, int(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

num_prime = 0
x = 1
while num_prime < 10001:
    x += 1
    if is_prime(x):
        num_prime += 1

print x
