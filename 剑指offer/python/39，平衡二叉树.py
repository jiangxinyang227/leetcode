"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

解题思路，每个节点的左子树和右子树的深度差小于等于1，则该树为平衡二叉树，否则不是，本题基本上是在求二叉树的深度上的扩展
"""


class Solution:

    def __init__(self):
        self.flag = True

    def is_balance(self, root):
        self.tree_iteration(root)
        return self.flag

    def tree_iteration(self, root):
        if not root or not self.flag:
            return 0
        left = self.tree_iteration(root.left)
        right = self.tree_iteration(root.right)
        if abs(left - right) > 1:
            self.flag = False
        return left + 1 if left > right else right + 1
