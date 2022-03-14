# python3
def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search_leftmost(keys, n, query):

    low = 0
    high = n

    while low < high:
        mid = (low + high) // 2
        if keys[mid] < query:
            low = mid + 1
        else:
            high = mid
    return low


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4

    high = len(keys) - 1
    low = 0

    return binary_search_single(keys, low, high, query)


def binary_search_single(keys, low, high, query):
    if query == keys[low]:
        return low

    if high > low:
        mid = low + (high - low)//2

        # middle element matches query
        if query == keys[mid]:
            return binary_search_leftmost(keys, mid, query)

        # query is smaller than middle element, so possibly present in left side before mid
        elif query < keys[mid]:
            return binary_search_single(keys, low, mid-1, query)

        # query is larger than middle element, so possibly present in right side after mid
        else:
            return binary_search_single(keys, mid+1, high, query)

    else:
        # query doesn't exist in array
        return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
