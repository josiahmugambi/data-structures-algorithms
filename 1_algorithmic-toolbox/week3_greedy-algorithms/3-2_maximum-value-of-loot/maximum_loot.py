# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    # sort spices by most value descending.
    # Output is a sorted catalogue with list of tuples of weights: unit price)
    unit_prices = [p / w for w, p in zip(weights, prices)]
    catalogue = sorted(zip(weights, unit_prices), key=lambda x: x[1], reverse=True)

    # sorted list of weights:
    weights = [x[0] for x in catalogue]
    unit_prices = [x[1] for x in catalogue]

    loot_value = 0
    available = [0] * len(weights)
    for i in range(len(weights)):
        if capacity == 0:
            return loot_value
        a = min(weights[i], capacity)
        loot_value += (a * (unit_prices[i]))
        weights[i] -= a
        available[i] += a
        capacity -= a
    return(loot_value)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
