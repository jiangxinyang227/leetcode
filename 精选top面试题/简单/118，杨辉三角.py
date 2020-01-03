"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution:
    def generate(self, numRows):
        result = [[1], [1, 1]]
        if numRows <= 2:
            return result[:numRows]

        for i in range(2, numRows):
            temp = [1] + [sum(result[-1][i: i + 2]) for i in range(len(result[-1]) - 1)] + [1]
            result.append(temp)
        return result


s = Solution()
res = s.generate(5)
print(res)