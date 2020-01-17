"""
先从整个序列中选择一个最小的元素和第一个元素替换
循环接着从子序列中选择一个最小的值替换子序列中第一个元素
"""


def select_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]


array = [3, 2, 4, 5, 1, 6]
select_sort(array)
print(array)