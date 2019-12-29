"""
众数是指在数组中出现次数大于n/2的元素
可以用投票的方法实现，时间复杂度O(N)，空间复杂度O(1)

求众数可以用这种方法，但是如果只是求数组中出现最多的元素，这种方法就失效了
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


nums = [1, 1, 1, 1, 1, 2, 3, 5, 4]
res = majority_element(nums)
print(res)
