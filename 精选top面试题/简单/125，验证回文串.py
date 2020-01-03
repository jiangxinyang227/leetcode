"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

"""


class Solution:
    def isPalindrome(self, s):
        s_list = []
        for char in s.lower():
            if 48 <= ord(char) <= 57 or 97 <= ord(char) <= 122:
                s_list.append(char)

        for i in range(len(s_list) // 2):
            if s_list[i] != s_list[len(s_list) - i - 1]:
                return False
        return True


string = "A man, a plan, a canal: Panama"
s = Solution()
res = s.isPalindrome(string)
print(res)
