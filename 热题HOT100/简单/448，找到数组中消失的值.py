"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

解法1，对于这种统计某个元素的个数，或者某个元素是否存在，都可以用哈希表来表示
解法2，对于存在的数字，我们在数字对应上的索引值标记为负值，之后统计每个索引位置上的值哪些为正，为正的就是缺失值

"""


class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            if nums[abs(num) - 1] < 0:
                continue
            nums[abs(num) - 1] *= -1

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result


a = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
res = s.findDisappearedNumbers(a)
print(res)
