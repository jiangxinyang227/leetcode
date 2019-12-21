"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

最简单的就是借助哈希表，统计下元素的频率，然后比较最大的次数是否超过一半
第二种方法：先采用求众数的方法，然后判断该数字出现的次数是否大于一半
"""


def more_than_half_num(numbers):
    map_dict = {}
    for number in numbers:
        if number not in map_dict:
            map_dict[number] = 0
        map_dict[number] += 1

    counter = sorted(map_dict.items(), key=lambda x: x[1], reverse=True)
    half = len(numbers) // 2
    if counter[0][1] > half:
        return counter[0][0]
    else:
        return 0


def more_than_half_num_1(numbers):
    if not numbers:
        return 0
    count = 0
    temp = numbers[0]

    for i in range(len(numbers) - 1):
        if temp == numbers[i]:
            count += 1
        else:
            count -= 1

        if count == 0:
            temp = numbers[i + 1]

    temp_total = 0
    for num in numbers:
        if temp == num:
            temp_total += 1

    if temp_total > len(numbers) // 2:
        return temp
    else:
        return 0




l = [1, 2, 3, 2, 4, 2, 5, 2, 3]
res = more_than_half_num(l)
print(res)


