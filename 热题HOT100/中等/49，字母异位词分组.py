"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for item in strs:
            count = self.convert_count(item)
            if d.get(count, 0):
                d[count].append(item)
            else:
                d[count] = [item]
        return list(d.values())

    def convert_count(self, string):
        result = [0] * 26
        for item in string:
            result[ord(item) - ord("a")] += 1
        return tuple(result)


s = Solution()
array = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = s.groupAnagrams(array)
print(res)