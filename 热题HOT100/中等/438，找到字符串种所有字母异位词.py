"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

滑动窗口的思想，用两个哈希表来存储滑动窗口的值和p的值
如果当前值不在p则直接去除。
"""


class Solution:

    def findAnagrams(self, s: str, p: str):
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []

        result = []
        left = right = 0
        map_p = {}
        windows = {}
        for char in p:
            map_p[char] = map_p.get(char, 0) + 1

        while right < len_s:
            temp_char = s[right]
            if temp_char not in map_p:
                # 如果当前的字符不在map_p中，则之前存的windows中的结果就无效了，直接清空，然后从下一步开始存
                windows.clear()
                left = right = right + 1
            else:
                windows[temp_char] = windows.get(temp_char, 0) + 1  # 把值存入到windows中
                if right - left + 1 == len_p:  # 如果滑窗的大小等于p的长度，就需要判断滑窗中的值是否和p相等
                    if windows == map_p:  # 如果相等，就将结果加进去
                        result.append(left)
                    windows[s[left]] -= 1  # 无论是否相等，当长度超过了p的长度都需要移除left的值，在这里将windows中left的值减1
                    left += 1  # left移动一位
                right += 1  # right移动一位
        return result


s = Solution()
res = s.findAnagrams("abab", "ab")
print(res)
