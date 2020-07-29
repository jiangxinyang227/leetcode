"""
二叉树的镜像
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return root
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)

    return root


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return None

        root.left, root.right = root.right, root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
        return root