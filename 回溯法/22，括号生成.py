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
        path = ""
        self.back_trace(n, result, path)
        return result

    def back_trace(self, n, result, path, left=0, right=0):
        if len(path) == 2 * n:
            result.append(path)
        if left < n:
            self.back_trace(n, result, path + "(", left + 1, right)
        if right < left:
            self.back_trace(n, result, path + ")", left, right + 1)


s = Solution()
res = s.generateParenthesis(3)
print(res)