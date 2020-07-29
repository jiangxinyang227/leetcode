"""
变态跳台阶
"""


def jump_floor_2(n):

    if n == 0:
        return 0
    return 2 ** (n - 1)


def jumpFloorII(number):
    # write code here
    n = 1
    if number == 1:
        return n
    for i in range(1, number):
        n *= 2
    return n


for i in range(10):
    print(jump_floor_2(i))
    print(jumpFloorII(i))
    print("------------")
