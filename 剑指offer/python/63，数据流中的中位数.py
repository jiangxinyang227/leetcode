"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。
"""


class Solution:
    def __init__(self):
        self.data = []

    def Insert(self, num):
        if not self.data:
            self.data.append(num)
        elif num > self.data[-1]:
            self.data.append(num)
        else:
            for i in range(len(self.data)):
                if self.data[i] > num:
                    self.data = self.data[:i] + [num] + self.data[i:]
                    break

    def GetMedian(self):
        length = len(self.data)
        if length % 2:
            return float(self.data[length // 2])
        return float((self.data[length // 2] + self.data[length // 2 - 1]) / 2)


s = Solution()
for item in [5, 2, 3, 4, 1, 6, 7, 0, 8]:
    s.Insert(item)
    print(s.GetMedian())
