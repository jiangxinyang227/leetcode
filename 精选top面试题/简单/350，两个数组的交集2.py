"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。


排序+双指针解法
利用哈希表法
"""


class Solution:
    # 哈希表法
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = {}
        for num in nums1:
            m[num] = m.get(num, 0) + 1

        k = 0
        for item in nums2:
            val = m.get(item, 0)
            if val > 0:
                nums1[k] = item
                k += 1
                m[item] = m.get(item) - 1
        return nums1[:k]

    def intersect1(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        length1 = len(nums1)
        length2 = len(nums2)

        p1, p2 = 0, 0
        result = []
        while p1 < length1 and p2 < length2:
            if nums1[p1] == nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return result


a1 = [4, 9, 5]
a2 = [9, 4, 9, 8, 4]
s = Solution()
result = s.intersect1(a1, a2)
print(result)
