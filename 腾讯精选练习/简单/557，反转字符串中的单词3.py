"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

"""


class Solution:
    def reverseWords(self, s):
        s_list = s.split(" ")
        new_s = ""
        for item in s_list:
            item_list = list(item)
            for i in range(len(item_list) // 2):
                item_list[i], item_list[len(item_list) - i - 1] = item_list[len(item_list) - i - 1], item[i]
            new_s += "".join(item_list) + " "
        return new_s.strip()


s = Solution()
res = s.reverseWords("hello world")
print(res)