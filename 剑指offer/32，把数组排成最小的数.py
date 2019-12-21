"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。

先转换数组中的元素成字符串，然后给出一个新的排序方法，即如果字符串拼接后：a+b > b+a，则a > b，反之亦然

"""


def print_min_numbers(numbers):
    if numbers is None or len(numbers) == 0:
        return ""
    numbers = list(map(str, numbers))
    pivot = numbers[0]
    less = [i for i in numbers[1:] if (pivot + i) > (i + pivot)]
    great = [i for i in numbers[1:] if (pivot + i) <= (i + pivot)]
    result = "".join(print_min_numbers(less)) + pivot + "".join(print_min_numbers(great))
    return result.lstrip("0")


a = [321, 3, 32]
res = print_min_numbers(a)
print(res)
