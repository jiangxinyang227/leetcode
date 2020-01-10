"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

排序，固定好一个数，然后用双指针夹逼逼近

"""


class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return []

        nums.sort()

        res = float("inf")

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum == target:
                    return target
                if abs(cur_sum - target) < abs(res - target):
                    res = cur_sum
                if cur_sum - target < 0:
                    left += 1
                else:
                    right -= 1
        return res


s = Solution()
result = s.threeSumClosest([-1, 2, 1, 4], 1)
print(result)