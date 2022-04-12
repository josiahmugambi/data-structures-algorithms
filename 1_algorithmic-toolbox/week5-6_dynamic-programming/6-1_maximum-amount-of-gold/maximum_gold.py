# python3

from sys import stdin


def maximum_gold(capacity, weights):
    # assert 1 <= capacity <= 10 ** 4
    # assert 1 <= len(weights) <= 10 ** 3
    # assert all(1 <= w <= 10 ** 5 for w in weights)

    max_gold = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    max_gold[0] = [weights[0] if weights[0] <= j else 0 for j in range(capacity + 1)]

    for i in range(1, len(weights)):
        for w in range(1, capacity + 1):
            max_gold[i][w] = max_gold[i - 1][w]
            if weights[i] <= w:
                val = max_gold[i - 1][w - weights[i]] + weights[i]
                if max_gold[i][w] < val:
                    max_gold[i][w] = val
    return max_gold[-2][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
