"""
合并两个排序链表
可以将一个链表中的值插入到另一个链表，并保持顺序
"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    head = Node(-1)
    cur = head

    while head1 is not None and head2 is not None:
        if head1.val <= head2.val:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        temp.next = None
        cur.next = temp
        cur = cur.next

    if head1 is None:
        cur.next = head2
    if head2 is None:
        cur.next = head1

    return head.next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.next = c
b.next = d
c.next = e
d.next = f

res = merge(a, b)
while res:
    print(res.val)
    res = res.next





