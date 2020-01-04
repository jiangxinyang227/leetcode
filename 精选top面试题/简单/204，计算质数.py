"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""
from math import sqrt


class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


s = Solution()
res = s.countPrimes(7)
print(res)