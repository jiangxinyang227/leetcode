"""
反转链表
取出后面的节点，在链表的表头插入
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    if head is None or head.next is None:
        return head

    pre = head
    cur = head.next
    while cur.next:
        pre.next = cur.next
        cur.next = head

        head = cur
        cur = pre.next

    pre.next = cur.next
    cur.next = head

    return cur


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


res = reverse_list(a)
while res:
    print(res.val)
    res = res.next

