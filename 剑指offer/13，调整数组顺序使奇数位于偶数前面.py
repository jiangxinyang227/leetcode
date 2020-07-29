"""
调整数组顺序，使得奇数位于偶数前面，并且保持奇数和偶数的相对位置
"""


def reorder_array(array):
    odd = []
    even = []

    for item in array:
        if item % 2:
            odd.append(item)
        else:
            even.append(item)
    return odd + even


class Solution:
    def reOrderArray(self, array):
        for i in range(1, len(array)):
            if array[i] % 2 and array[i-1] % 2 == 0:
                for j in range(i, 0, -1):
                    if array[j-1] % 2 == 0:
                        array[j], array[j-1] = array[j-1], array[j]
        return array


s = Solution()
res = s.reOrderArray([1, 3, 5, 2, 4, 8, 7])
print(res)


