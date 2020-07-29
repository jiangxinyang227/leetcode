"""
输出链表中倒数第k个节点
可以采用快慢指针，一个先走k步，另一个开始走
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def find_kth_to_tail(head, k):
    if head is None:
        return None

    fast = head
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    low = head

    while fast:
        fast = fast.next
        low = low.next
    return low.val


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None

        slow = head
        fast = head

        for i in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        return slow.val


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


res = find_kth_to_tail(a, 2)
s = Solution()
res1 = s.FindKthToTail(a, 4)
print(res)
print(res1)