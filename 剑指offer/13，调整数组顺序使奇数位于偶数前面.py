"""
调整数组顺序，使得奇数位于偶数前面，并且保持奇数和偶数的相对位置
"""


def reorder_array(array):
    odd = []
    even = []

    for item in array:
        if item % 2:
            odd.append(item)
        else:
            even.append(item)
    return odd + even



