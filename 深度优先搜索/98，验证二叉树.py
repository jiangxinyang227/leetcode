class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.is_valid(root)

    def is_valid(self, root):
        if root.left is None and root.right is None:
            return True
        if root.left is None:
            if root.right.val > root.val:
                return self.is_valid(root.right)
            else:
                return False
        if root.right is None:
            if root.left.val < root.val:
                return self.is_valid(root.left)
            else:
                return False
        if root.left.val < root.val < root.right.val:
            return self.is_valid(root.left) and self.is_valid(root.right)
        return False


a = TreeNode(2)
c = TreeNode(2)
a.left, a.right = None, c

s = Solution()
res = s.isValidBST(a)
print(res)