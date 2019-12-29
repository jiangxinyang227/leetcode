"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

如果当前字符流没有存在出现一次的字符，返回#字符。
"""


def first_appearing_once(s):
    d = {}

    for index, char in enumerate(s):
        if char not in d:
            d[char] = [index, 1]
        else:
            d[char][1] += 1

    first_index = len(s)
    for char, val in d.items():
        if val[1] == 1:
            first_index = min(first_index, val[0])
    if first_index == len(s):
        return "#"
    return s[first_index]


string = "google"
res = first_appearing_once(string)
print(res)