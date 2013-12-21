sum_squares = sum((x**2 for x in xrange(101)))
square_sums = sum((x for x in xrange(101)))**2
print square_sums - sum_squares
