"""

"""


def find_kth_largest(nums, k):
    def partition(left, right):
        """
        每次都去数组最左边的值作为pivot来将数组分割成两个部分
        :param left:
        :param right:
        :return:
        """
        pivot = nums[right]

        store_index = left  # 用来确定之后pivot放置的位置，而且该位置的值是大于pivot的，因为一开始就会和pivot做对比
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
        nums[store_index], nums[right] = nums[right], nums[store_index]

        return store_index

    def select(left, right, k_smallest):
        if left == right:
            return nums[left]

        # find the pivot position in a sorted list
        pivot_index = partition(left, right)

        if k_smallest == pivot_index:
            return nums[pivot_index]

        if k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)

        if k_smallest > pivot_index:
            return select(pivot_index + 1, right, k_smallest)

    return select(0, len(nums) - 1, len(nums) - k)


array = [3, 2, 1, 5, 6, 4]
res = find_kth_largest(array, 2)
print(res)