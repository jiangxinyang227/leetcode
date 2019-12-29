"""
按位与操作
"""


def number_of_one(n):
    count = 0
    while n != 0:
        count += 1
        n = (n - 1) & n
    return count


def number_of_one_1(n):

    if n < 0:
        n = n & 0xffffffff

    count = 0

    while n != 0:
        remainder = n % 2
        if remainder == 1:
            count += 1
        n = n // 2
    return count


for i in range(10):
    print(number_of_one(i))
    print(number_of_one_1(i))
    print("----------------")
