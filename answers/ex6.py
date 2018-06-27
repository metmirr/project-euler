"""
    Problem 6:
    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
"""


from functools import reduce

squre1 = reduce(lambda acc, x: x**2 + acc, range(1, 101))
squre2 = reduce(lambda acc, x: x + acc, range(1, 101))**2

print('answer:', squre2 - squre1)

