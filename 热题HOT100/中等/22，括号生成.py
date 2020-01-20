"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution:

    def generateParenthesis(self, n: int):
        result = []
        self.back_track(result, n)
        return result

    def back_track(self, result, n, path="", left=0, right=0):
        if len(path) == 2 * n:
            result.append(path)
            return

        if left < n:
            self.back_track(result, n, path + "(", left + 1, right)

        if right < left:
            self.back_track(result, n, path + ")", left, right + 1)


s = Solution()
res = s.generateParenthesis(3)
print(res)
