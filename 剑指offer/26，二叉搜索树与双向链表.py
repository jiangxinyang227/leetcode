"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向

注释：二叉搜索树中的左子树中所有的节点都小于根节点，右子树中所有的节点都大于根节点，
按照中序遍历得到的序列就是有序序列
另外是要得到一个双向链表，因此可以让左指针指向上一个节点，右指针指向下一个节点。
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.list_head = None
        self.list_tail = None

    def convert(self, root):
        # write code here
        if root is None:
            return

        self.convert(root.left)
        if self.list_head is None:  # 这一步可以拿到最左边的叶子节点作为链表的其实节点和终止节点
            self.list_head = root
            self.list_tail = root
        else:  # 移动链表的终止节点
            self.list_tail.right = root
            root.left = self.list_tail
            self.list_tail = root
        self.convert(root.right)
        return self.list_head



