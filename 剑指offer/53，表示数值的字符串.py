"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


def is_numeric(s):
    is_allow_dot = True
    is_allow_e = True
    for i in range(len(s)):
        if s[i] in "+-" and (i == 0 or s[i - 1] in "eE") and i < len(s) - 1:
            continue
        elif is_allow_dot and s[i] == ".":
            is_allow_dot = False
            if i >= len(s) - 1 or s[i + 1] not in "0123456789":
                return False
        elif is_allow_e and s[i] in "Ee":
            is_allow_dot = False
            is_allow_e = False
            if i >= len(s) - 1 or s[i + 1] not in "0123456789+-":
                return False
        elif s[i] not in "0123456789":
            return False
    return True


string = "5e2"
res = is_numeric(string)
print(res)