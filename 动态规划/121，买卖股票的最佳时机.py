"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        min_val = prices[0]
        max_diff = 0
        for temp in prices[1:]:
            max_diff = max(max_diff, temp - min_val)
            min_val = min(min_val, temp)
        return max_diff

    def maxProfit1(self, prices):
        dp_i_0, dp_i_1 = 0, float("-inf")
        for price in prices:
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, -price)
        return dp_i_0


s = Solution()
res = s.maxProfit([7, 1, 5, 3, 6, 4])
res1 = s.maxProfit1([7, 1, 5, 3, 6, 4])
print(res)
print(res1)
