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


class Solution:
    def maximalSquare(self, matrix) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp = [[0 for j in range(col + 1)] for i in range(row + 1)]
        max_val = 0

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_val = max(max_val, dp[i][j])
        return max_val


s = Solution()

