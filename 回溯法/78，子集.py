"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

import copy


class Solution:
    def subsets(self, nums):
        result = []
        path = []
        self.back_trace(nums, result, path)
        return result

    def back_trace(self, nums, result, path):
        result.append(copy.deepcopy(path))
        for i in range(len(nums)):
            path.append(nums[i])
            self.back_trace(nums[i+1:], result, path)
            path.pop()


s = Solution()
res = s.subsets([1, 2, 3])
print(res)