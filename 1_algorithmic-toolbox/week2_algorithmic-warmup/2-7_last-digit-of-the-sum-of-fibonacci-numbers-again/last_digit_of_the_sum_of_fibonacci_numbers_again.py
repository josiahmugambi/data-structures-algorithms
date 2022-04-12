# python3

def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    if n <= 1:
        return n
    f_list = list(range(0, n+1))
    f_list[0] = 0
    f_list[1] = 1

    for i in range(2, n+1):
        f_list[i] = f_list[i-1] % 10 + f_list[i-2] % 10
    return f_list[n] % 10


def p_period_length(m):
    previous, current = 0, 1
    for i in range(0, m**2):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    m = 10
    p_period = p_period_length(m)
    n = n % p_period
    if n <= 1:
        return n
    f_list = list(range(0, n+1))
    f_list[0] = 0
    f_list[1] = 1
    for i in range(2, n + 1):
        f_list[i] = last_digit_of_fibonacci_number(i-1) + last_digit_of_fibonacci_number(i-2)
    return sum(f_list) % m


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index <= 1:
        return to_index
    if from_index == 0:
        from_index_sum_last = from_index
    else:
        from_index_sum_last = last_digit_of_the_sum_of_fibonacci_numbers(from_index - 1)
    to_index_sum_last = last_digit_of_the_sum_of_fibonacci_numbers(to_index)

    return (to_index_sum_last - from_index_sum_last) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
