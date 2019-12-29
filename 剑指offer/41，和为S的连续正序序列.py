"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

因为是连续的整数序列，则有对于一个子序列，如果该子序列的值小于给定的值，则应该加上下一个值，
如果大于该值，则去除序列中的第一个值，当序列中第一个值大于设定值的一半时，停止循环，
因为是整数序列，因此从1开始
"""


def find_continues_sequence(tsum):
    result = []
    a, b = 1, 2
    while a <= tsum // 2:
        temp = list(range(a, b + 1))
        if sum(temp) == tsum:
            result.append(temp)
            a += 1
            b += 1
        elif sum(temp) < tsum:
            b += 1
        else:
            a += 1
    return result


res = find_continues_sequence(100)
print(res)
