class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []

    def binaryTreePaths(self, root):
        result = []
        if root is None:
            return result
        self.back_trace(root, result, "")
        return result

    def back_trace(self, root, result, path):
        path += str(root.val)
        if root.left is None and root.right is None:
            result.append(path)
            return
        if root.left:
            self.back_trace(root.left, result, path + "->")
        if root.right:
            self.back_trace(root.right, result, path + "->")


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(5)
a.left, a.right = b, c
c.right = d

s = Solution()
res = s.binaryTreePaths(a)
print(res)