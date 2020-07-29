"""
给定一个哨兵点，然后按照该点将小于该点的值放在左边，大于该点的值放在右边，依次对左右子序列递归
"""


def partition(nums, left, right):
    pivot_val = nums[right]
    split_index = left  # split_index会一直指在第一个大于pivot_val上或者前面
    for i in range(left, right):
        if nums[i] < pivot_val:
            nums[i], nums[split_index] = nums[split_index], nums[i]
            split_index += 1
    nums[split_index], nums[right] = nums[right], nums[split_index]
    return split_index


def quick_sort(nums, left, right):
    if left < right:
        split_index = partition(nums, left, right)
        quick_sort(nums, left, split_index - 1)
        quick_sort(nums, split_index, right)


array = [3, 2, 4, 5, 1, 6]
quick_sort(array, 0, 5)
print(array)