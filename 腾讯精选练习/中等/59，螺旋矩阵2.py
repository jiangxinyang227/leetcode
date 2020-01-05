"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution:
    def generateMatrix(self, n):
        result = [[0 for j in range(n)] for i in range(n)]

        row_s = 0
        row_e = n
        col_s = 0
        col_e = n

        val = 1
        while val <= n ** 2:
            for i in range(col_s, col_e):
                result[row_s][i] = val
                val += 1
            row_s += 1

            for j in range(row_s, row_e):
                result[j][col_e - 1] = val
                val += 1
            col_e -= 1

            for k in range(col_e, col_s, -1):
                result[row_e - 1][k - 1] = val
                val += 1
            row_e -= 1

            for l in range(row_e, row_s, -1):
                result[l - 1][col_s] = val
                val += 1
            col_s += 1

        return result


s = Solution()
res = s.generateMatrix(3)
print(res)
