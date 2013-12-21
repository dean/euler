def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def get_matrix(n):
    for x in xrange(n):
        for y in xrange(n):
            yield x*y

mults = get_matrix(1000)
print max((x for x in mults if is_palindrome(x)))
