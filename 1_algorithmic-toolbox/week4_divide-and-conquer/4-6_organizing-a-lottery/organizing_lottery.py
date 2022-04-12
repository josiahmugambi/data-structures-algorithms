# python3
from sys import stdin
# from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    cnt = {}
    c = 0

    # Really tried to do dac but couldn't figure it out and ran out of itme
    # Solution via https://github.com/huyvohcmc/coursera-dsa/blob/master/algorithmic-toolbox/3-divideandconquer-starter-files/points_and_segments.py
    #
    # Comments my own to aid my understanding
    # This feels a bit like a dynamic approach
    #
    #
    # Example:
    #  start = [0, 0, -5], end = [3, 2, 1] and points = [3, 1, 0]))
    #
    # 1) create an list of tuples from start + end + points marking each point as (l)eft of (p)oint or to its (r)ight. Result:
    #          [(0, 'l'), (0, 'l'), (-5, 'l'), (3, 'p'), (1, 'p'), (0, 'p'), (3, 'r'), (2, 'r'), (1, 'r')]
    #
    #

    line = [(s, 'l') for s in starts]
    line += [(p, 'p') for p in points]
    line += [(e, 'r') for e in ends]

    # 2) sort list in place: Result:
    #          [(-5, 'l'), (0, 'l'), (0, 'l'), (0, 'p'), (1, 'p'), (1, 'r'), (2, 'r'), (3, 'p'), (3, 'r')]

    line.sort()

    # 3) go through list and progressively apply (c)ost: (l)eft: +1, (r)ight: -1, point: insert in current (c)ost in  dict cnt location x[0] where x is current point :
    #           [(-5, 'l'), (0, 'l'),  (0, 'l'),  (0, 'p'),        (1, 'p'),        (1, 'r'),    (2, 'r'),    (3, 'p'),     (3, 'r')]
    #           c=0, +1     c=1, +1,   c=2, +1,   c=3, cnt[0]=c,  c=3, cnt[1]=c,    c=3, -1,     c=2, -1,     c=1, cnt[3],  c=1, -1           c = 0
    #

    for x in line:
        if x[1] == 'l':
            c += 1
        elif x[1] == 'r':
            c -= 1
        else:
            cnt[x[0]] = c

    # 4) cnt now contains:  {0: 3, 1: 3, 3: 1} where the keys are the points, and the values are the number of segments
    #    return and convert to list and return the list of values ordered by initial index of points
    #

    return [cnt[p] for p in points]


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
