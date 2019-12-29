"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。

"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_(root):
    if root is None:
        return []

    result = []
    cur_nodes = [root]
    is_even = True
    while cur_nodes:
        cur_values = []
        next_nodes = []
        for node in cur_nodes:
            cur_values.append(node.val)
            if node.left is not None:
                next_nodes.append(node.left)
            if node.right is not None:
                next_nodes.append(node.right)
        cur_nodes = next_nodes
        result.append(cur_values if is_even else cur_values[::-1])
        is_even = not is_even

    return result


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

res = print_(a)
print(res)
