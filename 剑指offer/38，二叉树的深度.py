"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

在二叉树中很多解题的方法都可以用递归来实现，因为左子树和右子树又可以看作一颗二叉树，这种特性决定了很容易使用递归
例如这里求根节点的深度，等于左节点和右节点中的最大深度加一
"""


def tree_depth(root):
    if root is None:
        return 0

    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)
    return max(left_depth, right_depth) + 1