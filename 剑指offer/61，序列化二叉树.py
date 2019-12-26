"""
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(root):
    if root is None:
        return "#"
    return str(root.val) + serialize(root.left) + serialize(root.right)


def deserialize(s):
    vals = list(s)

    def build():
        if vals:
            val = vals.pop(0)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = build()
            root.right = build()
            return root

    return build()


def bfs(root):
    if root is None:
        return None
    queue = [root]
    while queue:
        pop_node = queue.pop(0)
        print(pop_node.val)
        if pop_node.left is not None:
            queue.append(pop_node.left)
        if pop_node.right is not None:
            queue.append(pop_node.right)


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

res = serialize(a)
print(res)

root = deserialize(res)
bfs(root)