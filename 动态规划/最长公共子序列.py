"""
基于动态对话的公共最长子序列计算
text1 = “abcde”
text2 = "ace"
则公共子序列为"ace"

根据动态规划认为整体的最优问题可以转换成子问题的最优问题
因此有：
对于最后的字符，如果相等，则最优问题为text1[len(text1)-1]和text2[len(text2) - 1]的最优子序列+1。
如果不等，则为text1[len(text1)]，text2[len(text2) - 1]和text1[len(text1)-1]，text2[len(text2)]的最大值。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)

        # 将text1做行，text2做列
        table = [[0 for col in range(length2 + 1)] for row in range(length1 + 1)]
        # 先遍历行，再遍历列
        for i in range(1, length1 + 1):
            for j in range(1, length2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
        return table[-1][-1]


a = "ylqpejqbalahwr"
b = "yrkzavgdmdgtqpg"

s = Solution()
res = s.longestCommonSubsequence(a, b)
print(res)
