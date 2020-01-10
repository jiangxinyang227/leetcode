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


class Solution:
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


s = Solution()
res = s.subsets([1, 2, 3])
print(res)