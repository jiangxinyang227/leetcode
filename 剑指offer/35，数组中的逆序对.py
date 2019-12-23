"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

copy一个数组，对该数组进行排序，拿到当前的最小值，判断该值在元素组中的位置，该位置为该值存在的逆序对，
当计算下一个值时，需要将之前的最小值从原数组中去除
"""


def inverse_pairs(data):
    sort_data = sorted(data)
    count = 0
    for i in sort_data:
        pos = data.index(i)
        count += pos
        data.pop(pos)
    res = count % 1000000007
    return res


nums = [3, 2, 1, 4, 5, 6, 7, 0]
result = inverse_pairs(nums)
print(result)
