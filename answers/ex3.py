"""
    Problem 3:
    What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % 2 == 0:
            return False
    return True


class Prime:
    def __init__(self):
        self.curr = 1

    def __next__(self):
        new_next = self.curr + 1
        while not is_prime(new_next):
            new_next += 1
        self.curr = new_next

        return self.curr

    def __iter__(self):
        return self


num = 600851475143
largest = 0

for i in Prime():
    if num % i == 0:
        largest = i
    while num % i == 0 and num >=2:
        num = num // i

    if num == 1:
        break

print('answer:', largest)
