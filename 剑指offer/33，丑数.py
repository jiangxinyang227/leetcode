"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


def get_ugly_number(index):
    if index == 0:
        return 0
        # 1作为特殊数直接保存
    all_num = [1]
    min2 = min3 = min5 = 0
    total = 1
    while total < index:
        min_num = min(all_num[min2] * 2, all_num[min3] * 3, all_num[min5] * 5)
        all_num.append(min_num)
        # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
        while all_num[min2] * 2 <= min_num:
            min2 += 1
        # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
        while all_num[min3] * 3 <= min_num:
            min3 += 1
        # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
        while all_num[min5] * 5 <= min_num:
            min5 += 1
        total += 1
    return all_num[-1]


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return None
        result = [1]
        index2, index3, index5 = 0, 0, 0
        total = 1
        while total < index:
            min_val = min(result[index2] * 2, result[index3] * 3, result[index5] * 5)
            result.append(min_val)
            if result[index2] * 2 <= min_val:
                index2 += 1
            if result[index3] * 3 <= min_val:
                index3 += 1
            if result[index5] * 5 <= min_val:
                index5 += 1
            total += 1
        return result[-1]


n = 7
res = get_ugly_number(n)
print(res)
s = Solution()
res1 = s.GetUglyNumber_Solution(7)
print(res1)