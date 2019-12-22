"""
两数相加，可以创建一个哨兵节点用来开始存储生成的新的链表
"""


class ListNode(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def add_two_numbers(l1, l2):
    pre_node = ListNode(0)
    cur = pre_node

    prefix = 0
    while l1 or l2:
        if l1 is None:
            l1_val = 0
        else:
            l1_val = l1.val

        if l2 is None:
            l2_val = 0
        else:
            l2_val = l2.val

        temp = l1_val + l2_val + prefix
        reminder = temp % 10
        temp_node = ListNode(reminder)
        cur.next = temp_node
        cur = cur.next
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
        prefix = temp // 10

    if prefix != 0:
        cur.next = ListNode(prefix)

    return pre_node.next


h1 = ListNode(2)
a = ListNode(4)
b = ListNode(3)
h1.next = a
a.next = b

h2 = ListNode(5)
c = ListNode(6)
# d = ListNode(4)
h2.next = c
# c.next = d

res = add_two_numbers(h1, h2)
while res is not None:
    print(res.val)
    res = res.next
