"""
    Problem 7:
    What is the 10 001st prime number?
"""


def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
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


pos = 0
for i in Prime():
    pos += 1
    if pos == 10001:
        print('answer:', i)
        break
