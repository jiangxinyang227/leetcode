"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

示例 1:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:

输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。


本题完全可以利用搜索树的性质，也就是父节点的左子树中所有值小于父节点，同理右子树大于父节点
因此可以根据当前节点的值是否介于两个节点值之间来判断该节点是不是最近公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p is None or q is None:
            return None

        if p.val > q.val:
            p, q = q, p

        while root is not None:
            print(root.val)
            print(p.val)
            print(q.val)
            if p.val <= root.val <= q.val:
                return root
            elif p.val > root.val:
                root = root.right
            else:
                root = root.left
        return None


# a = TreeNode(6)
# b = TreeNode(2)
# c = TreeNode(8)
# d = TreeNode(0)
# e = TreeNode(4)
# f = TreeNode(7)
# g = TreeNode(9)
# h = TreeNode(3)
# i = TreeNode(5)
#
# a.left, a.right = b, c
# b.left, b.right = d, e
# c.left, c.right = f, g
# g.left, g.right = h, i
a = TreeNode(2)
b = TreeNode(1)
a.left = b

s = Solution()
res = s.lowestCommonAncestor(a, a, b)
print(res.val)