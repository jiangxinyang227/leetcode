"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。

先用快慢指针判断有没有环，然后将一个指针从head开始，和慢指针同时走，相遇的位置即为环的入口

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return None

        slow = head.next
        fast = head.next.next

        while slow != fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is None or fast.next is None:
                return None

        # 如果有环
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b

s = Solution()
res = s.detectCycle(a)
print(res.val)
