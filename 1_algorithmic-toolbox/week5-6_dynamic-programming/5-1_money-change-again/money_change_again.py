# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    min_num_coins = [0]
    coins = [1, 3, 4]
    for m in range(1, money + 1):
        min_num_coins.append(float("inf"))
        for c in coins:
            if m >= c:
                num_coins = min_num_coins[m-c] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
