"""
采用双指针+后指针，从最后的位置开始遍历比较大小
"""


def merge(nums1, m, nums2, n):
    if nums1 == [] or nums2 == []:
        return nums1

    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1

        p -= 1
    nums1[:p2 + 1] = nums2[:p2 + 1]

    return nums1


a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
res = merge(a, 3, b, 3)
print(res)