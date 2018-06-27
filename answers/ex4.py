"""
    Problem 4:
    Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_polindrome(n):
    return str(n) == str(n)[::-1]


polindrome = 0

for i in range(100, 999):
    for j in range(100, 999):
        if is_polindrome(i * j) and i * j > polindrome:
            polindrome = i * j


print('answer: %d' %polindrome)

