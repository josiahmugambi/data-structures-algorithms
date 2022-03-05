# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    number_of_coins = 0
    denomination = [10, 5, 1]
    for d in denomination:
        result = divmod(money, d)
        money = money - (result[0] * d)
        number_of_coins += result[0]
        if result[1] == 0:
            return number_of_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
