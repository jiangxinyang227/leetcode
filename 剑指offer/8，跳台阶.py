"""
跳台阶，本质上是费波切纳数列
"""


def jump_floor(number):
    a, b = 1, 2
    if number == 0:
        return 0
    for i in range(1,number):
        a, b = b, a + b

    return a


for i in range(10):
    print(jump_floor(i))