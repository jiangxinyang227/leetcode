"""
对于一个排序的数组，将数组的后半段放到前半段，该数组称为旋转数组，寻找该数组中的最小数字
因为数据本质上是排序数组，所以可以用二分查找，但是在这里的数组中可能存在元素重复的现象
"""


def min_num_in_rotate_array(rotate_array):
    left = 0
    right = len(rotate_array) - 1
    while left < right:
        mid = int((left + right) / 2)
        if rotate_array[mid] > rotate_array[right]:
            left = mid + 1
        elif rotate_array[mid] < rotate_array[right]:
            right = mid
        else:
            right -= 1
    return rotate_array[left]


a = [3, 3, 1, 1, 2, 3]
res = min_num_in_rotate_array(a)
print(res)
