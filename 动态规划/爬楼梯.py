"""
可以用动态规划解，也可以直接用费波切纳数列解
"""


def climb_stairs(n):
    a, b = 1, 1
    for i in range(1, n):
        a, b = b, a + b
    return b


s = 3
res = climb_stairs(s)
print(res)
