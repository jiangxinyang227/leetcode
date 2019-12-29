"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

方法一：可以用递归的方法一个节点一个节点的复制
方法二：分三步走，首先复制节点放在当前节点的后一位，其次将复制的节点random指针指向上一节点的random节点的next，最后将
        原链表和复制链表分离。
"""


class RandomListNode(object):
    def __init__(self, val):
        self.label = val
        self.next = None
        self.random = None


# 递归实现
def clone(head):
    if head is None:
        return
    new_node = RandomListNode(head.label)
    new_node.random = head.random
    new_node.next = clone(head.next)
    return new_node


# 三步走实现
def clone1(head):
    if head is None:
        return None

    # 第一步，先复制链表上的节点，放在当前节点的后面，例如
    # A->B->C 复制后就是A->A'->B->B'->C->C'
    cur = head
    while cur:
        next_node = cur.next  # 这里存下下一个节点，防止在引入复制节点后，找不到下一个原节点
        copy_node = RandomListNode(cur.label)
        copy_node.next = next_node
        cur.next = copy_node
        cur = next_node

    # 第二步，将复制的node的random指针指向原节点的random节点的下一个节点
    cur = head
    while cur:
        random_node = cur.random  # 存下原节点的random节点
        copy_node = cur.next  # copy 节点
        if random_node:
            copy_node.random = random_node.next
        cur = copy_node.next  # 跳过copy节点

    # 第三步，分离原链表和复制链表，在这里不用管random指针，因为random指针都是指向自己链表中的节点的
    cur = head
    copy_head = head.next
    while cur:
        copy_node = cur.next
        next_node = copy_node.next
        cur.next = next_node
        if next_node:
            copy_node.next = next_node.next
        else:
            copy_node.next = None  # 如果原节点的下一个节点是空，我们需要为复制节点重新创造一个空节点
        cur = next_node

    return copy_head


