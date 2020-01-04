"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
 

注意事项：您可以假定该字符串只包含小写字母。

"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s):
        d = defaultdict(int)
        for i, temp in enumerate(s):
            d[temp] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


s = Solution()
res = s.firstUniqChar("leetcode")
print(res)