"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

基本思路：快慢指针
首先判断是否有环，如果无环返回None
有环再寻找入环口
"""


def entry_node_of_loop(head):
    if head is None or head.next is None or head.next.next is None:
        return None

    slow = head.next
    fast = head.next.next

    while slow != fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is None:
            return None
        else:
            if fast.next is None:
                return None

    # 如果有环
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
