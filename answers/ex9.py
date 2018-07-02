"""
    Problem 9:
    There exists exactly one Pythagorean triplet for which
    a + b + c = 1000. Find the product abc.
"""

for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print('answer:', a*b*c)

