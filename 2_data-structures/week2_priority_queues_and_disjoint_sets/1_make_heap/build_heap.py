# python3
swaps = []
data = []
size = 0

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def sift_down(i):
    global size
    global data
    global swaps
    
    min_index = i 
    l = left_child(i) 
    if l <= size and data[l] < data[min_index]:
        min_index = l 

    r = right_child(i)     
    if r <= size and data[r] < data[min_index]:
        min_index = r 
        
    if i != min_index:
        swaps.append([i, min_index])
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(min_index)


def build_heap(data):
    global size
    for i in range ( size //2, -1, -1):
        sift_down(i)
    
    return swaps



def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


def main():
    global data
    global swaps
    global size

    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    size = len(data) - 1
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
