"""
暴力方法解决
"""


def max_sub_array(array):
    max_value = array[0]
    temp = array[0]
    for item in array[1:]:
        if item > temp + item:
            temp = item
        else:
            temp += item
        max_value = max(temp, max_value)
    return max_value


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = max_sub_array(nums)
print(res)
