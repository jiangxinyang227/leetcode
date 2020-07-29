"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""


class Solution:
    def maxSubArray(self, nums):
        """
        动态规划：if nums[i] + dp[i-1] < 0 dp[i] = 0  else dp[i] = dp[i-1] + nums[i]
        :param nums:
        :return:
        """
        length = len(nums)
        dp = [0 for i in range(length + 1)]
        for i in range(1, length + 1):
            if nums[i - 1] + dp[i - 1] < 0:
                continue
            dp[i] = nums[i - 1] + dp[i - 1]
        max_val = max(dp)
        if max_val == 0:
            return max(nums)
        return max(dp)

    def maxSubArray1(self, nums):
        """
        空间优化为O(1)
        :param nums:
        :return:
        """
        result = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            if temp < 0:
                temp = nums[i]
            else:
                temp += nums[i]
            result = max(temp, result)
        return result


s = Solution()
res = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
res1 = s.maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(res)
print(res1)