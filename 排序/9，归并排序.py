def merge(nums, left, mid, right):
    i, j = left, mid + 1
    temp = []
    while i <= mid and j <= right:
        if nums[i] < nums[j]:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    temp += nums[i:mid+1] or nums[j: right+1]

    # 拍完序后替换之前的数组
    for k in range(left, right + 1):
        nums[k] = temp[k - left]


def merge_sort(nums, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)
        merge(nums, left, mid, right)


array = [3, 2, 4, 5, 1, 6, 7, 9, 8]
merge_sort(array, 0, 8)
print(array)
