"""
栈的压入，弹出序列

解题思路：用一个栈来存储出栈的值，如果遇到出栈的值和入栈的值相等或者临时栈的值和入栈的值相等，就去除里面的值，
最后只要临时栈为空，则为true
"""


def is_pop_order(push_v, pop_v):
    stack = []

    while len(pop_v) > 0:
        if pop_v[-1] == push_v[-1]:
            pop_v.pop()
            push_v.pop()

        else:
            if not stack:
                stack.append(pop_v.pop())
            else:
                if stack[-1] == push_v[-1]:
                    stack.pop()
                    push_v.pop()
                else:
                    stack.append(pop_v.pop())

    for i in range(len(push_v)):
        if stack[-1] == push_v[-1]:
            stack.pop()
        push_v.pop()

    if not stack:
        return True
    return False


l1 = [1, 2, 3, 4, 5]
l2 = [3, 5, 4, 2, 1]

res1 = is_pop_order(l1, l2)
print(res1)
