"""
用哈希表实现
"""


def two_sum(nums, target):
    temp = {}
    for index, num in enumerate(nums):
        if target - num not in temp:
            temp[num] = index
        else:
            return [temp[target - num], index]


array = [2, 7, 11, 15]
n = 9
res = two_sum(array, n)
print(res)