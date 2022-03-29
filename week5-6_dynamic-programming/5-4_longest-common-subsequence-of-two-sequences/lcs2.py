# python3


def lcs2(a, b):
    # assert len(a) <= 100
    # assert len(b) <= 100

    al = len(a)
    bl = len(b)

    seq_table = [[0 for _ in range(bl + 1)] for _ in range(al + 1)]

    for i in range(al + 1):
        for j in range(bl + 1):
            if i == 0 or j == 0:
                seq_table[i][j] = 0
            elif a[i-1] == b[j-1]:
                seq_table[i][j] = 1 + seq_table[i-1][j-1]
            else:
                seq_table[i][j] = max(seq_table[i-1][j], seq_table[i][j-1])

    return seq_table[al][bl]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
