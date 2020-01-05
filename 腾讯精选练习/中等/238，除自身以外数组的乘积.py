"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

"""


class Solution:
    def productExceptSelf(self, nums):
        result = []

        pre = 1
        for i in range(len(nums)):
            result.append(pre)
            pre *= nums[i]

        back = 1
        for j in range(len(nums), 0, -1):
            result[j - 1] *= back
            back *= nums[j - 1]
        return result


s = Solution()
res = s.productExceptSelf([1, 2, 3, 4])
print(res)
