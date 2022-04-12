# python3

# from itertools import product
from sys import stdin


def subset3_sum(subset, n, s1, s2, s3):

    # 3 empty sub-sets means that they are equal
    if s1 == 0 and s2 == 0 and s3 == 0:
        return 1

    # base case
    if n < 0:
        return 0

    # becomes part of subset 1
    in_s1 = 0
    if s1 - subset[n] >= 0:
        in_s1 = subset3_sum(subset, n - 1, s1 - subset[n], s2, s3)

    # becomes part of subset 2
    in_s2 = 0
    if not in_s1 and (s2 - subset[n] >= 0):
        in_s2 = subset3_sum(subset, n - 1, s1, s2 - subset[n], s3)

    # becomes part of subset 3
    in_s3 = 0
    if (not in_s1 and not in_s2) and (s3 - subset[n] >= 0):
        in_s3 = subset3_sum(subset, n - 1, s1, s2, s3 - subset[n])

    return in_s1 or in_s2 or in_s3


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    total = sum(values)

    # return 0 if sum of values % 3 is not 0 implying that each partition sum will not be an integer
    # number of values should be at least 3
    if total % 3 != 0 or len(values) < 3:
        return 0

    sub3_total = total / 3

    n = len(values) - 1

    return subset3_sum(values, n, sub3_total, sub3_total, sub3_total)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
