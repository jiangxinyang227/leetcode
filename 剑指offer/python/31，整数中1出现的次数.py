"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13
因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

问题是从1到n之间的所有整数中1出现的次数
最简单粗暴的方法就是就不同位数上的值判断是不是1就可以了
"""


def number_of_1(n):
    result = 0
    for num in range(1, n + 1):
        while num != 0:
            if num % 10 == 1:
                result += 1
            num = num // 10
    return result


number = 99
res = number_of_1(number)
print(res)