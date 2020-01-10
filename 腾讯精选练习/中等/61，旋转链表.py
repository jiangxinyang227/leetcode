"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        # 1，先求链表的长度
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        # 2，将k对链表长度取余数
        k = k % length

        # 3，移动到倒数第k个位置
        pre = head
        cur = head.next
        for i in range(length - k - 1):
            pre = pre.next
            cur = cur.next

        if cur is None:
            return head

        while cur.next:
            cur = cur.next

        cur.next = head
        head = pre.next
        pre.next = None

        return head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
res = s.rotateRight(a, 2)
while res:
    print(res.val)
    res = res.next
