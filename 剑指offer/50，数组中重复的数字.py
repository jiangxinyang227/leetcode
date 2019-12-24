"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
那么对应的输出是第一个重复的数字2。

解题思路：从前往后开始遍历，如果当前值和当前索引相等，则下一个，如果当前值和当前索引不相等，则比较当前值和以当前值为
索引的值，相等则返回，不相等就交换
"""


def duplicate(numbers, duplication):
    for i, val in enumerate(numbers):
        if i != val:
            if val != numbers[val]:
                numbers[i], numbers[val] = numbers[val], numbers[i]
            else:
                duplication.append(val)
                return True
    return False


n = [2, 3, 1, 0, 2, 5, 3]
d = []
res = duplicate(n, d)
print(res)
print(d)
