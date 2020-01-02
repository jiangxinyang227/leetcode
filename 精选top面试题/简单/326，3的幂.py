"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。
"""


class Solution:
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0