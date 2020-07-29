"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

"""


class Solution:
    def countBits(self, num: int):
        """
        解题思路，对于奇数，只需要在上一个偶数的比特位值的最后一位改成1；对于偶数，正好等于除以2的上一个值，因为正好向前进一个位
        :param num:
        :return:
        """
        dp = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp


s = Solution()
res = s.countBits(5)
print(res)
