"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7

注意: 合并必须从两个树的根节点开始。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def merge_trees(self, t1, t2):
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        root = TreeNode(t1.val + t2.val)
        root.right = self.merge_trees(t1.right, t2.right)
        root.left = self.merge_trees(t1.left, t2.left)
        return root

    def bfs(self, root):
        if root is None:
            return []

        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            print(pop_node.val)
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)


tree1 = TreeNode(1)
a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(5)
tree1.left, tree1.right = a, b
a.left = c

tree2 = TreeNode(2)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(7)
tree2.left, tree2.right = d, e
d.right, e.right = f, g

s = Solution()
tree = s.merge_trees(tree1, tree2)
s.bfs(tree)