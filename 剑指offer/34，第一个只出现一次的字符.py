"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
如果没有则返回 -1（需要区分大小写）
"""


def first_not_repeating_char(s):
    d = {}
    for item in s:
        if item not in d:
            d[item] = 0
        d[item] += 1

    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1


string = "abcabdd"
res = first_not_repeating_char(string)
print(res)