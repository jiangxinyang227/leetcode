"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (not matrix):
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        pre = 0
        dp = [0] * (n + 1)
        for i in range(0, m):
            for j in range(1, n + 1):
                tmp = dp[j]
                if (matrix[i][j - 1] == "1"):
                    dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                    res = max(dp[j], res)
                else:
                    dp[j] = 0
                pre = tmp
            pre = 0
        return res * res
