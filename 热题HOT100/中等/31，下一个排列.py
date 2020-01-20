"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""


class Solution:
    def nextPermutation(self, nums) -> None:
        first_index = -1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                first_index = i - 1
                break
        if first_index == -1:
            self.reverse(nums, 0, n - 1)
            return

        second_index = -1
        for j in range(n - 1, first_index, -1):
            if nums[j] > nums[first_index]:
                second_index = j
                break

        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        self.reverse(nums, first_index + 1, n - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


s = Solution()
array = [2, 3, 1]
s.nextPermutation(array)
print(array)
