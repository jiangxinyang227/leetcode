"""
输入两个链表，找出它们的第一个公共结点。

对于两个链表，如果有公共节点，则第一个公共节点后面的节点都是公共的
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def find_first_common_node(head1, head2):

    p1 = head1
    p2 = head2

    # 首先计算出两个链表的长度
    length1 = 0
    length2 = 0
    while p1:
        length1 += 1
        p1 = p1.next

    while p2:
        length2 += 1
        p2 = p2.next

    # 然后让两个链表中的指针在距离尾部同一长度的节点处
    p1 = head1
    p2 = head2

    if length1 > length2:
        for i in range(length1 - length2):
            p1 = p1.next
    else:
        for j in range(length2 - length1):
            p2 = p2.next

    while p1 and p2:
        if p1 == p2:
            break
        p1 = p1.next
        p2 = p2.next

    return p1


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)

a.next = b
b.next = c
c.next = f
f.next = g
d.next = e
e.next = f


res = find_first_common_node(a, d)
print(res.val)
