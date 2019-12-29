"""
费波切纳数列的应用
"""


def rect_cover(n):
    if n == 0:
        return 0

    a, b = 1, 2
    for i in range(1, n):
        a, b = b, a + b
    return a


for i in range(10):
    print(rect_cover(i))