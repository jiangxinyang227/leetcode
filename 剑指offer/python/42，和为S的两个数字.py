"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。

因为是一个增序的序列，因此可以从头部和尾部给定两个指针来控制，首先找出所有的数字对，然后给出乘积最小的一对
"""


def find_numbers_with_sum(array, tsum):
    left = 0
    right = len(array) - 1
    result = []
    while left < right:
        temp = array[left] + array[right]
        if temp == tsum:
            result.append([array[left], array[right]])
            left += 1
        elif temp < tsum:
            left += 1
        else:
            right -= 1

    if not result:
        return []

    result = sorted(result, key=lambda x: x[0] * x[1], reverse=False)
    return result[0]


a = [1, 2, 3, 4, 5, 6]
res = find_numbers_with_sum(a, 7)
print(res)