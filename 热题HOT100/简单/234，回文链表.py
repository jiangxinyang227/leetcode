"""
请判断一个链表是否为回文链表。

输入: 1->2
输出: false

输入: 1->2->2->1
输出: true


你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
最简单的方法，借助一个list来存储链表中所有的值，然后判断列表是否为回文列表，时间复杂度O（n）,空间复杂度O（n）

另一种方法，时间复杂度O（n）,空间复杂度O（1）.采用快慢指针，找到链表的中间位置，然后将后半段反转，反转完之后将慢指针作为
后半段的初始位置，然后另一个从head开始遍历，判断head指向的值和慢指针指向的值是否相等。
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):

    @staticmethod
    def is_palindrome(head):
        if head is None:
            return True
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        list_len = len(val_list)
        for i in range(list_len // 2):
            if val_list[i] != val_list[list_len - (i + 1)]:
                return False
        return True

    def reverse_list(self, head):
        """
        反转链表
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head

        pre = head
        cur = head.next
        while cur:
            pre.next = cur.next
            cur.next = head
            head = cur
            cur = pre.next
        return head

    def is_palindrome_1(self, head):
        """
        将链表的后半段反转，然后比较前半段和后半段的值
        :param head:
        :return:
        """
        if head is None:
            return True
        if head.next is None:
            return False
        # 1，找到后半段序列
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # 反转后半段
        new_slow = self.reverse_list(slow)
        while new_slow:
            if head.val != new_slow.val:
                return False
            head = head.next
            new_slow = new_slow.next
        return True


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(2)
e = ListNode(1)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
res = s.is_palindrome_1(a)
print(res)


