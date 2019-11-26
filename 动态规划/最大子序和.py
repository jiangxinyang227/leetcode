"""
动态规划解法
"""


def max_sub_array(array):
    max_value = array[0]  # 存储最大值
    temp = array[0]  # 存储当前值
    for item in array[1:]:
        if item > temp + item:
            temp = item
        else:
            temp += item
        max_value = max(temp, max_value)
    return max_value


"""
用分治法+递归实现
思路：对于一条序列从中间分割，则最大子序和要么出现在左边的序列，要么在右边的序列，要么发生在中间，即左边的一部分加上
右边的一部分，因此可以求这三个部分的最大子序和，然后取最大值返回
"""


def max_sub_array_1(array):
    length = len(array)
    mid_index = length // 2
    if length == 1:
        return array[0]
    else:
        max_left = max_sub_array_1(array[:mid_index])
        max_right = max_sub_array_1(array[mid_index:])

    # 求中间的最大子序和
    max_l = 0
    temp_l = 0
    for i in range(mid_index-1, -1, -1):
        temp_l += array[i]
        max_l = max(max_l, temp_l)

    max_r = 0
    temp_r = 0
    for j in range(mid_index, length):
        temp_r += array[j]
        max_r = max(max_r, temp_r)

    return max(max_left, max_right, max_l + max_r)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = max_sub_array_1(nums)
print(res)
