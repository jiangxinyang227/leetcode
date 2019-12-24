"""
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0

输入一个字符串,包括数字字母符号,可以为空

如果是合法的数值表达则返回该数字，否则返回0
"""


def str_to_int(s):
    if s == "":
        return 0

    flag = 1
    res = 0
    if s[0] in "+-":
        if s[0] == "-":
            flag *= -1
        s = s[1:]

    rev_s = s[::-1]
    for i, char in enumerate(rev_s):
        if char not in "0123456789":
            return 0
        res += (ord(char) - ord("0")) * (10 ** i)
    res = flag * res
    if -2 ** 31 <= res < 2 ** 31:
        return res
    return 0


string = "123456"
result = str_to_int(string)
print(result)