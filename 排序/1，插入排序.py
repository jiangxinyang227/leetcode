"""
从第一个元素开始，和第0个元素对比，先排序好这两个元素，然后依次拿后面的元素和前面的元素比较
第i个元素和前i个元素比较，通过从和i-1 一直到0，和各个元素比较交换，当不满足条件时就停止交换
"""


def insert_sort(nums):
    for i in range(1, len(nums)):
        while i > 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i -= 1


array = [3, 2, 4, 5, 1, 6]
insert_sort(array)
print(array)
