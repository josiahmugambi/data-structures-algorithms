# python3

from random import randint


def partition3(array, left, right):
    m1 = left
    index = left
    m2 = right

    pivot = array[left]

    while index <= m2:
        if array[index] < pivot:
            # push item to the left
            array[m1], array[index] = array[index], array[m1]
            m1 += 1
            index += 1
        elif array[index] > pivot:
            # push item to the right, beyond pivot
            array[index], array[m2] = array[m2], array[index]
            m2 -= 1
        else:
            index += 1

    return m1, m2


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    (m1, m2) = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
