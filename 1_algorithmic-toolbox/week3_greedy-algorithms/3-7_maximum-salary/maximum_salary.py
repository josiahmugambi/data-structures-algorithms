# python3

from itertools import permutations
from math import inf
import sys

def is_ge_or_eq(a, b):

    opt1 = int("".join(map(str, [a, b])))
    opt2 = int("".join(map(str, [b, a])))

    if opt1 >= opt2:
        answer = a
    else:
        answer = b

    return answer


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(digits):
    answer = []

    while len(digits) > 0:
        max_digit = -inf
        for digit in digits:
            if max_digit == -inf:
                max_digit = digit
            else:
                max_digit = is_ge_or_eq(digit, max_digit)
        answer.append(max_digit)
        digits.remove(max_digit)
    result = int(''.join(map(str, answer)))
    return result


if __name__ == '__main__':
#    n = int(input())
#    input_numbers = input().split()
#    assert len(input_numbers) == n
#    print(largest_number(input_numbers))

    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
