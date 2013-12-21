from math import sqrt

MAX_VAL = 600851475143

# Inefficient, but should solve within 2 mins.
def is_prime(n):
    for x in range(2, int(sqrt(n))):
        if n % x == 0:
            return False
    return True

primes = []
for x in xrange(2, int(sqrt(MAX_VAL))):
    if is_prime(x):
        primes.append(x)

max = 0
for x in primes:
    if MAX_VAL % x == 0:
        max = x

print max
