"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
    ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

对于二进制表示可以通过异或操作来获得不同位的数量，不同位值异或为1，相同位值异或为0，异或后只要统计1的数量即可

"""


class Solution:
    def hammingDistance(self, x, y):
        return bin(x^y).count("1")


s = Solution()
res = s.hammingDistance(1, 4)
print(res)