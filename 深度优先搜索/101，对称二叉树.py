class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.comparison(root.left, root.right)

    def comparison(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            return self.comparison(left.left, right.right) and self.comparison(left.right, right.left)
        return False


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g

s = Solution()
res = s.isSymmetric(a)
print(res)
