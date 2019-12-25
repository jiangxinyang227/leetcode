"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

因为是排序好的链表，所以只需要从头到尾遍历一遍
因为可能一开始就重复，因此需要一个临时的结点作为起始结点
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_duplication(head):
    temp_node = ListNode(-1)
    temp_node.next = head
    last = temp_node

    while head and head.next:
        if head.val == head.next.val:
            val = head.val
            while head and head.val == val:
                head = head.next
            last.next = head
        else:
            last = head
            head = head.next
    return temp_node.next


a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(3)
e = ListNode(4)
f = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

res = delete_duplication(a)

cur = res
while cur:
    print(cur.val)
    cur = cur.next