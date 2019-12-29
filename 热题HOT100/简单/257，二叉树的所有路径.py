"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        self.findTreePahts(root, self.result, "")
        return self.result

    def findTreePahts(self, root, result, path):
        if root.left is None and root.right is None:
            result.append(path + str(root.val))
            return
        if root.left:
            self.findTreePahts(root.left, result, path + str(root.val) + "->")
        if root.right:
            self.findTreePahts(root.right, result, path + str(root.val) + "->")


tree = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(5)
tree.left, tree.right = a, b
a.right = c

s = Solution()
res = s.binaryTreePaths(tree)
print(res)