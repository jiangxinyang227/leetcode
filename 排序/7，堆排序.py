"""
实现一个优先队列
"""


class PriorQueue(object):
    def __init__(self, queue=[]):
        self.queue = queue
        if self.queue:
            self.build_heap()

    def is_empty(self):
        return not self.queue

    def peek(self):
        if self.is_empty():
            return
        return self.queue[0]

    def enqueue(self, val):
        self.queue.append(None)
        self.sift_up(val)

    def sift_up(self, val):
        length = len(self.queue) - 1
        i, j = length, (length - 1) // 2
        while i > 0 and val < self.queue[j]:
            self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
            i, j = j, (j - 1) // 2
        self.queue[i] = val

    def dequeue(self):
        if self.is_empty():
            return None
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        val = self.queue.pop()
        if len(self.queue) > 0:
            self.sift_down(self.queue[0], 0, len(self.queue))
        return val

    def sift_down(self, val, begin, end):

        i = begin
        j = begin * i + 1
        while j < end:
            if j + 1 < end and self.queue[j + 1] < self.queue[j]:
                j += 1
            if val < self.queue[j]:
                break
            self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
            i, j = j, 2 * j + 1
        self.queue[i] = val

    def build_heap(self):
        end = len(self.queue)
        for i in range(end // 2, -1, -1):
            self.sift_down(self.queue[i], i, end)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    print(arr)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


array = [3, 2, 4, 5, 1, 6]
heap_sort(array)
print(array)
