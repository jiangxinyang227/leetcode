class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multi, res = 0, ""

        for item in s:
            if item == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif item == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= item <= '9':
                multi = multi * 10 + int(item)
            else:
                res += item
        return res


s = Solution()
res = s.decodeString("3[a]2[bc]")
print(res)
