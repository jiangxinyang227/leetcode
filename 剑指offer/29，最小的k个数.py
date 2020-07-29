"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

最直接的方法是排序，然后取前k个数，可以把时间复杂度控制在nlogn
"""


def get_least_numbers(nums, k):
    length = len(nums)
    if length < 1 or k > length:
        return []

    left = 0
    right = length - 1
    mid = partition(left, right, nums)
    while mid != k - 1:
        if mid > k - 1:
            right = mid - 1
            mid = partition(left, right, nums)
        else:
            left = mid + 1
            mid = partition(left, right, nums)
    res = nums[:mid + 1]
    return res


def partition(left, right, nums):
    pivot = nums[left]

    nums[left], nums[right] = nums[right], nums[left]

    store_index = left
    for i in range(left, right):
        if nums[i] < pivot:
            nums[i], nums[store_index] = nums[store_index], nums[i]
            store_index += 1
    nums[store_index], nums[right] = nums[right], nums[store_index]

    return store_index


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        left = 0
        right = len(tinput) - 1
        while left < right:
            store_index = self.partition(left, right, tinput)
            if store_index == k:
                return tinput[:store_index]
            elif store_index < k:
                left = store_index + 1
            else:
                right = store_index - 1

    def partition(self, left, right, tinput):
        pivot = tinput[right]
        store_index = left

        for i in range(left, right):
            if tinput[i] < pivot:
                tinput[i], tinput[store_index] = tinput[store_index], tinput[i]
                store_index += 1
        tinput[store_index], tinput[right] = tinput[right], tinput[store_index]
        return store_index


numbers = [4, 5, 1, 6, 2, 7, 3, 8]
result = get_least_numbers(numbers, 6)
print(numbers)
print(result)


s = Solution()
res = s.GetLeastNumbers_Solution(numbers, 4)
print(res)

