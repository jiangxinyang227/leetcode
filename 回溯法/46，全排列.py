"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


import copy


class Solution:
    def permute(self, nums):
        result = []
        path = []
        self.back_trace(nums, result, path)
        return result

    def back_trace(self, nums, result, path):
        """
        用递归来回溯
        :param nums:
        :param result:
        :param path:
        :return:
        """
        for i in range(len(nums)):
            path.append(nums[i])
            if len(path) < 3:
                self.back_trace(nums[:i] + nums[i+1:], result, path)
            else:
                result.append(copy.deepcopy(path))
            path.pop()


s = Solution()
res = s.permute([1, 2, 3])
print(res)