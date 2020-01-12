"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

因为数组是连续的，因此如果存在一个连续的子数组的和等于k，其索引为[m, n]，则必然后sum([0:n]) - sum([0:m]) = k
所以可以用一个哈希表来存储之前所有从0开始的子串的和以及个数，因为有的可能会重复，因为会有连续的子串的和为0的现象。

"""


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sum_val = 0
        count = 0

        d = {0: 1}
        for num in nums:
            sum_val += num
            if sum_val - k in d:
                count += d[sum_val - k]
            d[sum_val] = d.get(sum_val, 0) + 1
        return count


s = Solution()
res = s.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7)
print(res)
