"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。


解题思路：分别求出所有的树的左子树深度和右子树深度的和，然后选择最大的值返回，因为最大路径可能过根节点，也可能不过根节点

"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.tree_pair_depths = 0

    def tree_depth(self, root):
        if root is None:
            return 0
        left_depth = self.tree_depth(root.left)
        right_depth = self.tree_depth(root.right)
        return max(left_depth, right_depth) + 1

    def diameter_of_binary_tree(self, root):
        if root is None:
            return 0
        self.tree_pair_depths = max(self.tree_depth(root.left) + self.tree_depth(root.right), self.tree_pair_depths)
        self.diameter_of_binary_tree(root.left)
        self.diameter_of_binary_tree(root.right)
        return self.tree_pair_depths


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left, a.right = b, c
b.left, b.right = d, e

s = Solution()
res = s.diameter_of_binary_tree(a)
print(res)