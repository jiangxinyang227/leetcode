def shell_sort(nums):
    n = len(nums)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = int(gap / 2)


array = [3, 2, 4, 5, 1, 6]
shell_sort(array)
print(array)