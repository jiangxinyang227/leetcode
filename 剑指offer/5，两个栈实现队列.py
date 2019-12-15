"""
用两个栈实现队列，栈是先进后出，队列是先进先出
"""


class Queue(object):
    def __init__(self):
        self.stack1 = []  # 用来存储添加的元素
        self.stack2 = []  # 主要是用来作为辅助栈，实现队列的先进先出

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None

        elif len(self.stack2) > 0:
            val = self.stack2.pop()
            return val

        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            val = self.stack2.pop()

            return val


q = Queue()
q.push(1)
q.push(2)
val = q.pop()
print(val)
q.push(3)
print(q.pop())
print(q.pop())
print(q.pop())