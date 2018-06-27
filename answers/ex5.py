"""
    Problem 5:
    What is the smallest positive number that is evenly divisible by all of the 
    numbers from 1 to 20?
"""


def divide(n):
    for i in range(2, 21):
        if n % i != 0:
            return False
    return True


n = 21

while True:
    if divide(n):
        break
    n += 1

print('answer:', n)






