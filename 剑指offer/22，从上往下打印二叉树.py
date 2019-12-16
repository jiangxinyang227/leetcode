"""
从上往下，同层节点从左往右，这就是宽度遍历，bfs
解题思路：利用队列的先进先出的思想来实现
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return None

    queue = [root]
    temp = []
    while queue:
        pop_node = queue.pop(0)
        temp.append(pop_node.val)

        if pop_node.left is not None:
            queue.append(pop_node.left)

        if pop_node.right is not None:
            queue.append(pop_node.right)
    return temp


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(3)
d = TreeNode(2)
e = TreeNode(1)

a.left = b
a.right = c
b.left = d
b.right = e

res = bfs(a)
print(res)
