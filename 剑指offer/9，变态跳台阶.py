"""
变态跳台阶
"""


def jump_floor_2(n):

    if n == 0:
        return 0
    return 2 ** (n - 1)


for i in range(10):
    print(jump_floor_2(i))
