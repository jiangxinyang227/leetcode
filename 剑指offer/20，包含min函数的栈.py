"""
给定一个栈，给出返回其最小值函数，需要O（1）时间实现
解题思路：用一个最小栈来存储无重复排好序的元素
"""


class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val < self.min():
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if not self.min_stack and val == self.min():
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]


s = Stack()
s.push(3)
print(s.min())
s.push(1)
s.push(2)
print(s.min())
s.push(1)
print(s.min())
s.pop()
s.pop()
print(s.min())