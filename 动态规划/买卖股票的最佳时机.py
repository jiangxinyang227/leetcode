"""
动态规划求解
"""


def max_profit(array):
    min_val = array[0]
    max_diff = 0

    for item in array[1:]:
        diff = item - min_val
        max_diff = max(max_diff, diff)
        if item < min_val:
            min_val = item

    return max_diff


nums = [7, 1, 5, 3, 6, 4]
nums1 = [7, 6, 5, 4, 3, 2, 1]
res = max_profit(nums1)
print(res)
