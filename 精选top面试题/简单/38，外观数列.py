"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

"""


class Solution:
    def countAndSay(self, n):
        result = [1]

        for i in range(1, n):
            string = str(result[-1])
            temp = string[0]
            count = 1
            res = ""
            for char in string[1:]:
                if char == temp:
                    count += 1
                else:
                    res += str(count)+temp
                    temp = char
                    count = 1
            res += str(count) + temp
            result.append(int(res))
        return str(result[n-1])


s = Solution()
res = s.countAndSay(5)
print(res)
