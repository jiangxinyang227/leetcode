"""
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

"""


class Solution:
    def findUnsortedSubarray(self, nums):
        min_stack = []
        max_stack = []
        min_flag = True
        max_flag = True
        for i in range(len(nums)):
            if not min_stack or min_stack[-1] <= nums[i]:
                if min_flag:
                    min_stack.append(nums[i])
            else:
                while min_stack and min_stack[-1] > nums[i]:
                    min_stack.pop()
                min_flag = False

            if not max_stack or max_stack[-1] >= nums[len(nums) - i - 1]:
                if max_flag:
                    max_stack.append(nums[len(nums) - i - 1])
            else:
                while max_stack and max_stack[-1] < nums[len(nums) - i - 1]:
                    max_stack.pop()
                max_flag = False

        if len(nums) == len(min_stack) == len(max_stack):
            return 0
        return len(nums) - len(min_stack) - len(max_stack)


s = Solution()
a = [1, 2, 3, 4]
res = s.findUnsortedSubarray(a)
print(res)