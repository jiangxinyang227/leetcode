"""
采用双指针，一个指针判断当前值是不是0，另一个指针去寻找下一个非0的值
"""


def move_zeros(nums):
    if len(nums) < 2:
        return nums

    cur, next_ = 0, 1
    while next_ < len(nums):

        if nums[cur] != 0:
            cur += 1
            next_ += 1

        elif nums[next_] == 0:
            next_ += 1

        else:
            nums[cur], nums[next_] = nums[next_], nums[cur]
            cur += 1
            next_ += 1

    return nums


def move_zeros1(nums):
    """
    单指针指向第一个0，然后将后面的非0值和该值交换
    :param nums:
    :return:
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums


a = [0, 0]
res = move_zeros(a)
print(res)
