"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。

"""


class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        if k == 0:
            return nums
        # 第一次反转, 翻转整个序列
        for i in range(len(nums) // 2):
            nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]

        # 第二次翻转，翻转前半部分
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

        # 第三次反转，翻转后半部分
        for i in range(k, (k + len(nums)) // 2):
            nums[i], nums[len(nums) + k - i - 1] = nums[len(nums) + k - i - 1], nums[i]


array = [1, 2, 3]
s = Solution()
s.rotate(array, 4)
print(array)
