"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

解题思路，每个节点的左子树和右子树的深度差小于等于1，则该树为平衡二叉树，否则不是，本题基本上是在求二叉树的深度上的扩展
"""


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        left_depth = self.tree_depth(pRoot.left)
        right_depth = self.tree_depth(pRoot.right)
        if abs(left_depth - right_depth) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def tree_depth(self, root):
        if root is None:
            return 0
        return max(self.tree_depth(root.left), self.tree_depth(root.right)) + 1
