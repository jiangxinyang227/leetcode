"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩散法求解，在这里的中心数量有2n-1个，因为中心点可以是一个字母，也可以是两个字母。因此我们要将这
        2n-1个中心点考虑进去
        :param s:
        :return:
        """
        result = ""

        length = len(s)
        for center in range(length * 2 - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < length and s[left] == s[right]:
                if (right - left + 1) > len(result):
                    result = s[left: right + 1]
                left -= 1
                right += 1
        return result


s = Solution()
res = s.longestPalindrome("abadbbd")
print(res)