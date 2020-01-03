"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

"""


class Solution:
    def titleToNumber(self, s):
        bit = 26
        result = 0
        s = s[::-1]
        index = 0
        for char in s:
            result += bit ** index * (ord(char) - ord("A") + 1)
            index += 1
        return result


s = Solution()
res = s.titleToNumber("ZY")
print(res)