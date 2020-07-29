"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


import copy


class Solution:
    def permuteUnique(self, nums):
        result = []
        path = []
        nums.sort()
        self.back_trace(nums, result, path, len(nums))
        return result

    def back_trace(self, nums, result, path, length):
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            if len(path) < length:
                self.back_trace(nums[:i] + nums[i+1:], result, path, length)
            else:
                result.append(copy.deepcopy(path))
            path.pop()


s = Solution()
res = s.permuteUnique([1])
print(res)