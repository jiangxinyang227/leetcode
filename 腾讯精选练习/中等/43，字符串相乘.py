"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = []
        for index1, item1 in enumerate(num1[::-1]):
            temp_result = []
            for index2, item2 in enumerate(num2[::-1]):
                temp_result.append(int(item1) * int(item2) * 10 ** index2)
            result.append(sum(temp_result) * 10 ** index1)
        return str(sum(result))


s = Solution()
res = s.multiply("12", "12")
print(res)