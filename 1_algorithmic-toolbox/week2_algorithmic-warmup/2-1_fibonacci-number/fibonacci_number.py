# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n
    f_list = list(range(0, n+1))
    f_list[0] = 0
    f_list[1] = 1
    for i in range(2, n+1):
        f_list[i] = f_list[i-1] + f_list[i-2]
    return f_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
