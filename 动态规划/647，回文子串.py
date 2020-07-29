"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        所有的回文子串都可以用中心发散法来求解
        :param s:
        :return:
        """
        n = len(s)
        result = 0
        total = []
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                total.append(s[left:right+1])
                result += 1
                left -= 1
                right += 1
        print(total)
        return result


s = Solution()
res = s.countSubstrings("aaa")
print(res)