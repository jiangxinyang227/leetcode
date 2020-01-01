"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

异或解决该问题，相同的元素异或得到的值为0，而0异或任何值都为任何值，且存在连乘的操作

"""


class Solution:
    def singleNumber(self, nums):
        temp = nums[0]
        for num in nums[1:]:
            temp ^= num
        return temp


s = Solution()
a = [1, 2, 1, 2, 3, 4, 4]
res = s.singleNumber(a)
print(res)