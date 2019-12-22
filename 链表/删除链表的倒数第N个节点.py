"""
用两个指针，一个指针先走N步，然后两个指针同时走
"""


class ListNode(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def remove_nth_from_end(head, n):
    if head is None:
        return head

    p = ListNode(-1)
    p.next = head
    cur, pre = p, p

    for i in range(n):
        cur = cur.next

    while cur.next is not None:
        pre = pre.next
        cur = cur.next

    pre.next = pre.next.next
    head = p.next
    return head


h = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)

h.next = a
a.next = b
b.next = c

res = remove_nth_from_end(h, 2)
while res is not None:
    print(res.val)
    res = res.next