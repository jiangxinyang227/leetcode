"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.

"""


class Solution:
    def canPartition(self, nums):
        n = len(nums)
        target = sum(nums)
        if (target % 2 != 0):
            return False
        target //= 2
        pre = [False] * (target + 1)
        cur = [False] * (target + 1)
        pre[0] = True
        for i in range(1, target + 1):
            if (nums[0] == i):
                pre[i] = True
                break
        for i in range(1, n):
            for j in range(target + 1):
                if (j >= nums[i]):
                    cur[j] = pre[j] or (pre[j - nums[i]])
                else:
                    cur[j] = pre[j]
            pre = cur[:]
        return cur[-1]


