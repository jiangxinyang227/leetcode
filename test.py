from typing import List
from itertools import chain
import collections


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0

        i = 0
        while i < len(s):
            print(i)
            if s[i] == " ":
                i += 1
            else:
                if s[i] in "/*":
                    temp = s[i]
                    left = int(stack.pop())
                    i += 1
                    while s[i] == " ":
                        i += 1
                    right = int(s[i])
                    if temp == "/":
                        stack.append(str(left // right))
                    else:
                        stack.append(str(left * right))
                else:
                    stack.append(s[i])
                i += 1
        print(stack)
        if len(stack) == 1:
            return stack[0]
        while stack:
            right = int(stack.pop())
            temp = stack.pop()
            left = int(stack.pop())

            if temp == "+":
                res += (left + right)
            else:
                res += (left - right)
        return res


s = Solution()
res = s.calculate(" 3+5 / 2 ")
print(res)


