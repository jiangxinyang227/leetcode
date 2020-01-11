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
        if len(s) <= 1:
            return s

        answer = ""
        new_s = "#"
        for i in s:
            new_s += i + "#"

        strip = 1  # 往外扩散的距离，对于扩散相同距离的回文串，取最前面的，因此后面的更长的回文串才会替换前面的，否则不会替换

        for i in range(1, len(new_s) - 2):

            while i - strip >= 0 and i + strip < len(new_s) and new_s[i - strip:i + strip + 1] == new_s[
                                                                                                  i - strip:i + strip + 1][
                                                                                                  ::-1]:
                answer = new_s[i - strip:i + strip + 1]
                strip += 1

        a = ""
        for i in answer:
            if i != '#':
                a += i

        return a

    def longestPalindrome1(self, s: str) -> str:
        length = len(s)

        result = ""

        for center in range(2 * length - 1):
            left = center // 2
            right = left + center % 2

            while left >= 0 and right < length and s[left] == s[right]:
                if right - left + 1 > len(result):

                    result = s[left:right + 1]
                left -= 1
                right += 1
        return result


s = Solution()
res = s.longestPalindrome("abadbbd")
res1 = s.longestPalindrome1("abadbbd")
print(res)
print(res1)
