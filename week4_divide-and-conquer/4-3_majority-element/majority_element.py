# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    # assert len(elements) <= 10 ** 5
    # This was helpful in helping me debug - https://cs.lmu.edu/~ray/notes/algowarmup/

    if majority_element_value(elements) is None:
        return 0
    else:
        return 1


def majority_element_value(elements):

    # Base cases:
    # 1) if a single integer in array return None
    if len(elements) == 0:
        return None

    # 2) if a single integer in array return element value
    if len(elements) == 1:
        return elements[0]

    mid = len(elements) // 2

    left = majority_element_value(elements[0:mid])
    right = majority_element_value(elements[mid:])

    # if majority element matches on both sides of elements, return that value
    if left == right:
        return left

    # else check which side has a larger count for found majority array
    if elements.count(left) > mid:
        return left

    if elements.count(right) > mid:
        return right

    # return None if nothing is found
    return None


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
