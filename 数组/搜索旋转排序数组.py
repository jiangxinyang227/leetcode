"""
本质上还是排好序的数组，可以用二分查找
本题的思路是先确定mid值是在旋转点的左边还是右边，不同边的中间值的处理是不一样的
"""


def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if target > nums[mid]:
                left = mid + 1
            else:
                if target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        if nums[mid] <= nums[right]:
            if target < nums[mid]:
                right = mid - 1
            else:
                if target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

    return -1


a = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
n = 4
res = search(a, n)
print(res)
