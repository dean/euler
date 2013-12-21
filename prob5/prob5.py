import sys

def divisible_by_range(start, end, num):
    while start != end:
        if num % end != 0:
            return False
        end = end -1
    return True

n = 20
while True:
    if divisible_by_range(1, 20, n):
        print n
        sys.exit(0)
    n = n + 20
