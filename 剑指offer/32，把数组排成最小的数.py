"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。

先转换数组中的元素成字符串，然后给出一个新的排序方法，即如果字符串拼接后：a+b > b+a，则a > b，反之亦然

"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if numbers is None or len(numbers) == 0:
            return ""
        self.quick_sort(0, len(numbers) - 1, numbers)
        return "".join(list(map(str, numbers)))

    def quick_sort(self, left, right, numbers):
        if left < right:
            store_index = self.partition(left, right, numbers)
            self.quick_sort(left, store_index-1, numbers)
            self.quick_sort(store_index, right, numbers)

    def partition(self, left, right, numbers):
        pivot = numbers[right]
        store_index = left

        for i in range(left, right):
            if str(numbers[i]) + str(pivot) <= str(pivot) + str(numbers[i]):
                numbers[i], numbers[store_index] = numbers[store_index], numbers[i]
                store_index += 1
        numbers[store_index], numbers[right] = numbers[right], numbers[store_index]
        return store_index


a = [1, 11, 111]
s = Solution()
res = s.PrintMinNumber(a)
print(res)
