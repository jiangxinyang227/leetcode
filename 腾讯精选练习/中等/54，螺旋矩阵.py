"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

"""


class Solution:
    def spiralOrder(self, matrix):
        col_start = 0
        row_start = 0
        row_end = len(matrix)
        col_end = len(matrix[0])

        result = []

        while row_start < row_end and col_start < col_end:
            for num in matrix[row_start][col_start: col_end]:
                result.append(num)
            row_start += 1
            if row_start >= row_end:
                break

            for num in [array[col_end - 1] for array in matrix[row_start: row_end]]:
                result.append(num)
            col_end -= 1
            if col_start >= col_end:
                break

            for num in matrix[row_end - 1][col_start: col_end][::-1]:
                result.append(num)
            row_end -= 1
            if row_start >= row_end:
                break

            for num in [array[col_start] for array in matrix[row_start: row_end]][::-1]:
                result.append(num)
            col_start += 1
        return result


s = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8 , 9], [10, 11, 12]]
res = s.spiralOrder(a)
print(res)
