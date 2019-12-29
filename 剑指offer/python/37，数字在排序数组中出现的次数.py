"""
统计一个数字在排序数组中出现的次数。

因为是排序数组，因此只要找到这个数字，然后计算其个数，因为是排序数组，因此可以用二分查找其索引，然后统计其个数
"""


def get_number_of_k(data, k):
    index = get_k(data, k)
    if index == -1:
        return 0
    count = 0
    for item in data[:k][::-1]:
        if item == k:
            count += 1
        else:
            break

    for item in data[k:]:
        if item == k:
            count += 1
        else:
            break

    return count


def get_k(data, k):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == k:
            return mid
        elif data[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1


nums = [1, 2, 2, 2, 3]
res = get_number_of_k(nums, 2)
print(res)