"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

这道题的本质意思是给定一个链表，但是链表中的每个元素是一个二叉树，按照二叉树的中序遍历来返回下一个结点，所以就有
当该结点有右子树，则返回右子树中最左下方的值，否则返回下一个结点的最左下方值
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def get_next(node):
    if not node:
        return None
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        while node.next:
            if node == node.next.left:
                return node.next
            node = node.next
    return None
