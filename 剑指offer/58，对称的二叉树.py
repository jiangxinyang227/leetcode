"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

import copy


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symmetrical(root):
    if root is None:
        return True
    return comparison(root.left, root.right)


def comparison(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val == right.val:
        return comparison(left.left, right.right) and comparison(left.right, right.left)
    return False


a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(9)
d = TreeNode(5)
e = TreeNode(7)
f = TreeNode(7)
g = TreeNode(5)
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

res = is_symmetrical(a)
print(res)
