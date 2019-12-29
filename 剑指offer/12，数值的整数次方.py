"""
分段递归的思想，当在主函数中需要做判断的时候，可以将递归函数写到另一个函数里面
"""


def power(base, exp):
    if base == exp == 0:
        return None

    if exp >= 0:
        return power_value(base, exp)
    else:
        return 1 / power_value(base, abs(exp))


def power_value(base, exp):
    if exp == 1:
        return base
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return power_value(base, exp >> 1) ** 2
    else:
        return base * power_value(base, exp >> 1) ** 2


for i in range(5):
    print(power(2, i))
