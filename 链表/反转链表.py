"""
链表的反转，可以在o(n)时间内完成
"""


class ListNode(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def reverse_list(head):
    """
    链表只需要用一个头节点记录即可
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head

    pre = head
    cur = head.next
    while cur is not None:
        pre.next = cur.next
        cur.next = head
        head = cur

        cur = pre.next

    return head


h = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
h.next = a
a.next = b
b.next = c
c.next = d
d.next = None

print("before reverse")
cur = h
while cur is not None:
    print(cur.val)
    cur = cur.next

print("after reverse")

res = reverse_list(h)
while res is not None:
    print(res.val)
    res = res.next

