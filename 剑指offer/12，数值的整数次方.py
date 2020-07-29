"""
分段递归的思想，当在主函数中需要做判断的时候，可以将递归函数写到另一个函数里面
"""


class Solution:
    def power(self, base, exponent):
        if exponent < 0:
            return 1 / self.power_value(base, -exponent)
        return self.power_value(base, exponent)

    def power_value(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        mid = exponent // 2
        return self.power_value(base, mid) * self.power_value(base, exponent - mid)


s = Solution()
res = s.power(2.0000, -2)
print(res)
