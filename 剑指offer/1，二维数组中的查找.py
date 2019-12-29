"""
给定一个二维数组，其中的元素从左到右依次递增，从上到下依次递增
时间复杂度：O（m ✖ n）
空间复杂度：O（1）
"""


def find(array, target):
    if array == []:
        return False
    row = 0
    col = len(array[0]) - 1

    while row < len(array) and col >= 0:
        cur = array[row][col]

        if cur == target:
            return True
        elif cur < target:
            row += 1
        else:
            col -= 1
    return False


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = 10

res = find(a, t)
print(res)