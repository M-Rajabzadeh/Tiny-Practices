'''
Complete the square sum function so that it squares each number
 passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9
'''

def square_sum(numbers):
    total = 0
    for number in numbers:
        total += number ** 2
    return total


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)