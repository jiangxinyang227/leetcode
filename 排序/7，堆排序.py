"""
实现一个优先队列
"""


def sift_down(array, begin, end):
    father, son_left = begin, begin * 2 + 1
    while son_left < end:
        if son_left + 1 < end and array[son_left] < array[son_left + 1]:
            son_left += 1
        if array[son_left] < array[father]:
            break
        array[son_left], array[father] = array[father], array[son_left]
        father, son_left = son_left, son_left * 2 + 1


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)

    # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        sift_down(arr, 0, i)


array = [3, 2, 4, 5, 1, 6]
heap_sort(array)
print(array)
