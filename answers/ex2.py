"""
    Problem 2:
    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
"""


class Fib:
    def __init__(self):
        self.curr = 0
        self.next = 1

    def __next__(self):
        self.new_next = self.curr + self.next
        self.curr = self.next
        self.next = self.new_next
        if self.curr > 4000000:
            raise StopIteration
        return self.curr

    def __iter__(self):
        return self


answer = 0

for i in Fib():
    if i % 2 == 0:
        answer += i

print('answer:', answer)

