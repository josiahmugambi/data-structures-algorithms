# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    # table - store intermediate results
    # https://thisthread.blogspot.com/2018/02/primitive-calculator.html

    table = [0] * (n + 1)

    for t in range(1, len(table)):
        table[t] = table[t-1] + 1
        if t % 2 == 0:
            table[t] = min(table[t], table [t // 2] + 1 )
        if t % 3 == 0:
            table[t] = min(table[t], table [t // 3] + 1 )

    # return (table[-1] - 1)  #is the length of the list of sequences including

    sequence = [1] * table[-1]
    for t in range(1, table[-1]):
        sequence [-t] = n

        if table[n - 1] == table[n] - 1:
            n -= 1
        elif n % 2 == 0 and (table[n // 2] == table[n] - 1 ):
            n //= 2
        else:
            n //= 3
    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
