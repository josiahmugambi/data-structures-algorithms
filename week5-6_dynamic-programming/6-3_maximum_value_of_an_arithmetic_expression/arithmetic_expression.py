# python3


from math import inf
import re


def calculate(y, operator, z):
    if operator == "+":
        result = y + z
    elif operator == "-":
        result = y - z
    elif operator == "*":
        result = y * z
    else:
        result = y / z

    return result


def min_and_max(i, j, op, min_values, max_values):
    cmin = inf
    cmax = -inf
    for k in range(i, j):
        a = calculate((max_values[i][k]), op[k], max_values[k + 1][j])
        b = calculate((max_values[i][k]), op[k], min_values[k + 1][j])
        c = calculate((min_values[i][k]), op[k], max_values[k + 1][j])
        d = calculate((min_values[i][k]), op[k], min_values[k + 1][j])
        cmin = min(cmin, a, b, c, d)
        cmax = max(cmax, a, b, c, d)
    return cmin, cmax


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    nums = [int(i) for i in re.findall("\d", dataset)]
    op = re.findall("[-+*/]", dataset)

    n = len(nums)

    max_values = [[None for _ in range(n)] for _ in range(n)]
    min_values = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        min_values[i][i] = nums[i]
        max_values[i][i] = nums[i]

    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            min_values[i][j], max_values[i][j] = min_and_max(i, j, op, min_values, max_values)

    return max_values[0][n - 1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
