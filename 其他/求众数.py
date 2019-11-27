"""
可以用投票的方法实现，时间复杂度O(N)，空间复杂度O(1)
"""


def majority_element(array):
    temp = array[0]
    count = 0

    for i in range(len(array) - 1):
        if temp == array[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            temp = array[i + 1]

    return temp


nums = [3, 2, 3]
res = majority_element(nums)
print(res)
