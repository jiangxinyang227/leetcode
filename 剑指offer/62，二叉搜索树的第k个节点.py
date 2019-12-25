"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

根据二叉搜索树的特性，中序遍历得到的序列正好是从小到大排序的序列
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kth_node(root, k):
    if root is None:
        return None

    stack = []
    cur = root
    count = 0
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            count += 1
            pop_node = stack.pop()
            if count == k:
                return pop_node
            cur = pop_node.right

    return None


a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(10)
d = TreeNode(5)
e = TreeNode(7)
f = TreeNode(9)
g = TreeNode(11)

a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

res = kth_node(a, 1)
print(res.val)