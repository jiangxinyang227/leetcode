"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


def find_nums_appear_once(array):
    temp, mask, num1, num2 = 0, 1, 0, 0
    for i in range(len(array)):
        temp ^= array[i]
    while temp & 1 == 0:
        temp >>= 1
        mask <<= 1
    for i in range(len(array)):
        if array[i] & mask:
            num1 ^= array[i]
        else:
            num2 ^= array[i]
    return [num1, num2]


nums = [1, 1, 2, 2, 3, 4]
res = find_nums_appear_once(nums)
print(res)