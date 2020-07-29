"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。
对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。

将问题转换成动态规划问题
设带＋的部分和为x，带-的部分和为y，总和为s，目标值为t。则有：
x - y = t
x + y + x - y = t + s
2x = t + s
因此只要求数组中有多少的x等于（t + s）/ 2
"""


class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        s = sum(nums)
        if (s + S) % 2 or s < S:
            return 0

        target = (s + S) // 2

        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] + dp[i-num]
        return dp[-1]


s = Solution()
res = s.findTargetSumWays([1, 1, 1, 1, 1], 3)
print(res)