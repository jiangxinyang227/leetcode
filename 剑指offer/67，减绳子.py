"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""


def cut_rope(length):
    if length < 2: return 0
    if length == 2: return 1
    if length == 3: return 2

    # 其他情况，如果总的绳子长度=4，那么效果一样，最大乘积都是4
    # 如果绳子长度>=5,那么需要尽可能的多剪成长度为3的子绳子段,然后长度为2的绳子最多2段，不要留绳子长度为1的
    timesOf3 = length // 3
    if (length - timesOf3 * 3) == 1:  # length=4,7,10,如果是10=3*3*3*1或者3*（）
        timesOf3 -= 1
    timeOf2 = (length - timesOf3 * 3) // 2
    result = pow(3, timesOf3) * pow(2, timeOf2)
    return result
