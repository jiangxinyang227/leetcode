"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

    def lowestCommonAncestor1(self, root, p, q):
        """
        记录每个结点的父节点
        :param root:
        :param p:
        :param q:
        :return:
        """
        stack = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node_pop = stack.pop()
            if node_pop.left:
                parent[node_pop.left] = node_pop
                stack.append(node_pop.left)
            if node_pop.right:
                parent[node_pop.right] = node_pop
                stack.append(node_pop.right)

        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        while q:
            if q in ancestors:
                return q
            q = parent[q]
        return None


a = TreeNode(3)
b = TreeNode(5)
c = TreeNode(1)
d = TreeNode(6)
e = TreeNode(2)
f = TreeNode(0)
g = TreeNode(8)
h = TreeNode(7)
i = TreeNode(4)
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g
e.left, e.right = h, i

s = Solution()
res = s.lowestCommonAncestor1(a, b, i)
print(res.val)