"""
把最大的元素往后放
"""


def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


array = [3, 2, 4, 5, 1, 6]
bubble_sort(array)
print(array)
