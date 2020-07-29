"""
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""


class Solution:
    def maxProduct(self, nums) -> int:
        result = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            # pre_max保证前面的是正数，pre_min保证前面的是负数，num保证在上一个为0的情况下，重新从下一个开始
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            result = max(result, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return result


s = Solution()
res = s.maxProduct([2, 3, -2, 4])
print(res)
