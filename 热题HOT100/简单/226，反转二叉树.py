"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。

其实这道题就是二叉树的镜像
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    @staticmethod
    def bfs(root):
        if root is None:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(6)
g = TreeNode(9)
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

s = Solution()
res = s.invertTree(a)
s.bfs(res)
