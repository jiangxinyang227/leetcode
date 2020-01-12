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

整个算法的思路是先以单个字符为中心往两边扩散，如果扩散后的子字符串还是回文，则继续扩散，此时覆盖所有的奇数回文串
然后再以连续的两个字符串为中心往两边扩散，扩散同上

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        ans = 0
        for center in range(2 * length - 1):
            left = center // 2
            right = left + center % 2  # 为了覆盖奇偶现象
            while left >= 0 and right < length and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


s = Solution()
res = s.countSubstrings("abcbd")
print(res)