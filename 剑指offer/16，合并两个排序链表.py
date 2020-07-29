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

        cur.next = temp
        cur = cur.next

    if head1 is None:
        cur.next = head2
    if head2 is None:
        cur.next = head1

    return head.next


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHead = cur = Node(-1)
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next

            else:
                cur.next = pHead2
                pHead2 = pHead2.next

            cur = cur.next
        cur.next = pHead1 or pHead2
        return pHead.next


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

# res = merge(a, b)
# while res:
#     print(res.val)
#     res = res.next

s = Solution()
res1 = s.Merge(a, b)
while res1:
    print(res1.val)
    res1 = res1.next