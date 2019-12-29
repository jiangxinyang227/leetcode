"""
将字符串中的空格替换成 20%
"""


def replace_space(string):
    new_string = ""

    for item in string:
        if item == " " or item == "\t":
            new_string += "20%"
        else:
            new_string += item

    return new_string


s = "How are you?"
res = replace_space(s)
print(res)