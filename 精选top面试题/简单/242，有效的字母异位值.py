"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

注，两个字符串含有相同的字母，则被称为异位词
"""


class Solution:
    def isAnagram(self, s, t):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1

        for char in t:
            val = d.get(char, 0)
            if val > 0:
                d[char] = d.get(char) - 1
            else:
                return False
        return True


s = "ab"
t = "ba"
solution = Solution()
res = solution.isAnagram(s, t)
print(res)
