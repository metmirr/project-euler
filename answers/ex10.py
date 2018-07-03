"""
    Problem 10:
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.Find the sum of
    all the primes below two million.
"""


sum = 0
size = 2000000
slots = [True for i in range(size)]
slots[0] = False
slots[1] = False

for stride in range(2, size // 2):
    pos = stride
    while pos < size - stride:
        pos += stride
        slots[pos] = False

for idx, pr in enumerate(slots):
    if pr:
        sum += idx

print('answer:', sum)

