# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    inv, a = sort_count(a)
    return inv


def sort_count(a):
    if len(a) <= 1:
        return 0, a

    mid = len(a)//2
    inv_b, left = sort_count(a[0:mid])
    inv_c, right = sort_count(a[mid:])
    inv_bc, a_merged = count_cross_merge(left, right)

    inversions = inv_b + inv_c + inv_bc
    return inversions, a_merged


def count_cross_merge(left, right):
    merged = []
    i = j = inv = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            inv += len(left) - i
            j += 1
        else:
            merged.append(left[i])
            i += 1
    if i < len(left):
        merged.extend(left[i:])
    else:
        merged.extend(right[j:])
    return inv, merged


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
