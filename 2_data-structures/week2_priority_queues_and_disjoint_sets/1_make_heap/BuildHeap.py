# python3

class BuildHeap:
    def __init__(self, data, size):
        self._swaps = []
        self._data = data
        self._size = size
    
    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
    def parent(self, i):
        return i//2
    
    def answer(self):
        print(len(self._swaps))
        for i, j in self._swaps:
            print (i, j)
    
    def sift_down(self, i):
        min_index = i 
        l = self.left_child(i) 
        
        if l <= self._size and self._data[l] < self._data[min_index]:
            min_index = l 

        r = self.right_child(i)     

        if r <= self._size and self._data[r] < self._data[min_index]:
            min_index = r 
        
        if i != min_index:
            self._swaps.append([i, min_index])
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.sift_down(min_index)

    def build_heap(self):
        for i in range ( self._size //2, -1, -1):
            self.sift_down(i)

def main():

    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    size = len(data) - 1
    my_heap = BuildHeap(data, size)
    my_heap.build_heap()
    my_heap.answer()

    #print(len(swaps))
    #for i, j in swaps:
    #    print(i, j)


if __name__ == "__main__":
    main()
