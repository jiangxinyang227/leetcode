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
    def __init__(self):
        self.result = []

    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            print(res)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

    def subsets1(self, nums):
        """
        回溯法求解
        1, self.result：用来存储所有的解
        2，path：一个来存储临时可能的解
        3，index：控制模型的下一个选择
        4，path.pop()：往上一步回溯
        :param nums:
        :return:
        """
        self.back_track([], nums, 0)
        return self.result

    def back_track(self, path, nums, index):
        temp = copy.deepcopy(path)
        self.result.append(temp)
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.back_track(path, nums, i + 1)
            path.pop()


s = Solution()
res = s.subsets1([1, 2, 3])
print(res)
