"""
    Problem 1:
    Find the sum of all the multiples of 3 or 5 below 1000.
"""


def find_sum(number):
    answer = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            answer += i
    
    return answer


if __name__ == '__main__':
    print('answer: ', find_sum(1000))
