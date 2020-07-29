"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""


class Solution:
    d = {"2": "abc",
         "3": "def",
         "4": "ghi",
         "5": "jkl",
         "6": "mno",
         "7": "pqrs",
         "8": "tuv",
         "9": "wxyz"}

    def letterCombinations(self, digits: str):
        result = []
        path = []
        self.back_trace(digits, result, path, len(digits))
        return result

    def back_trace(self, nums, result, path, length):
        for i in range(len(nums)):
            for j in range(len(self.d[nums[i]])):
                path.append(self.d[nums[i]][j])
                if len(path) == length:
                    result.append("".join(path))
                else:
                    self.back_trace(nums[i + 1:], result, path, length)
                path.pop()


s = Solution()
res = s.letterCombinations("23")
print(res)