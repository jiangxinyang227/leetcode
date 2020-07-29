"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""

import copy


class Solution:
    def subsetsWithDup(self, nums):
        result = []
        path = []
        nums.sort()  # 一定要排序，因为是要按照后面是否和前面重复来筛选的，所以要将相同的元素排列在一起
        self.back_trace(nums, result, path)
        return result

    def back_trace(self, nums, result, path):
        result.append(copy.deepcopy(path))
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.back_trace(nums[i + 1:], result, path)
            path.pop()


s = Solution()
res = s.subsetsWithDup([4, 4, 4, 1, 4])
print(res)