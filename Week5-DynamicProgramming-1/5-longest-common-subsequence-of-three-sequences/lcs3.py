# python3


def lcs3(a, b, c):
    # assert len(a) <= 100
    # assert len(b) <= 100
    # assert len(c) <= 100

    al = len(a)
    bl = len(b)
    cl = len(c)

    seq_table = [[[0 for _ in range(cl + 1)]
                  for _ in range(bl + 1)]
                 for _ in range(al + 1)]

    for i in range(al + 1):
        for j in range(bl + 1):
            for k in range(cl + 1):
                if i == 0 or j == 0 or k == 0:
                    seq_table[i][j][k] = 0
                elif a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    seq_table[i][j][k] = 1 + seq_table[i-1][j-1][k-1]
                else:
                    seq_table[i][j][k] = max(seq_table[i-1][j][k], seq_table[i][j-1][k], seq_table[i][j][k-1])
    return seq_table[al][bl][cl]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
