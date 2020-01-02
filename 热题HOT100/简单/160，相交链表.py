"""
编写一个程序，找到两个单链表相交的起始节点。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。


"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        p1 = headA
        p2 = headB

        length1 = 0
        length2 = 0
        while p1:
            length1 += 1
            p1 = p1.next

        while p2:
            length2 += 1
            p2 = p2.next

        p1 = headA
        p2 = headB
        if length1 > length2:
            for i in range(length1 - length2):
                p1 = p1.next
        else:
            for i in range(length2 - length1):
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

s = Solution()
res = s.getIntersectionNode(a, d)
print(res.val)