"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution:

    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return []
        nums.sort()
        result = []
        for i in range(length):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                print(i, left, right)
                temp = nums[i] + nums[left] + nums[right]
                if temp == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif temp > 0:
                    right -= 1
                else:
                    left += 1
        return result


s = Solution()
res = s.threeSum([-1, 0, 1, 2, -1, -4])
print(res)
