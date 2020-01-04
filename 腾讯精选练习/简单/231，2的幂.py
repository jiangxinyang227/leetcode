"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

"""


class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        while n > 2:
            print(n)
            print(type(n))
            if isinstance(n, float):
                return False
            n = n / 2
            if int(n) < n:
                return False
            n = int(n)
        return (n % 2 == 0)

    def isPowerOfTwo1(self, n):
        """
        位运算，对于2的幂，有n&(n-1) == 0
        :param n:
        :return:
        """
        return n > 0 and n & (n - 1) == 0


s = Solution()
res = s.isPowerOfTwo(8)
print(res)
