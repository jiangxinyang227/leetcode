"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

"""


class Solution:
    def minPathSum(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for j in range(col)] for i in range(row)]

        for i in range(row):
            for j in range(col):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    def minPath1(self, grid):
        row = len(grid)
        col = len(grid[0])
        dp = [0 for i in range(row)]
        for j in range(col):
            for i in range(row):
                if i == j == 0:
                    dp[i] = grid[i][j]
                elif i == 0:
                    dp[i] = dp[i] + grid[i][j]
                elif j == 0:
                    dp[i] = dp[i - 1] + grid[i][j]
                else:
                    dp[i] = min(dp[i], dp[i - 1]) + grid[i][j]
            print(dp)
        return dp[-1]


s = Solution()
res = s.minPathSum([[1, 2], [1, 1]])
res1 = s.minPath1([[1, 2], [1, 1]])
print(res)
print(res1)
