# python3


def edit_distance(s, t):
    m = len(s)
    n = len(t)
    distance = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            insertion = distance[i][j-1] + 1
            deletion = distance[i-1][j] + 1
            match = distance[i-1][j-1]
            mismatch = distance[i-1][j-1] + 1
            if i == 0:
                distance[i][j] = j
            elif j == 0:
                distance[i][j] = i
            elif s[i-1] == t[j-1]:
                distance[i][j] = min(insertion, deletion, match)
            else:
                distance[i][j] = min(insertion, deletion, mismatch)

    return distance[m][n]


def max_value(inputlist):
    return max([sublist[-1] for sublist in inputlist])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
