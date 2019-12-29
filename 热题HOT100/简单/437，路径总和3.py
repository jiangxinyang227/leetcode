"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

使用栈来遍历所有的序列

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        if root is None:
            return 0
        total = 0
        stack = [[root, [root.val]]]

        while stack:
            pop_node, temp_list = stack.pop()
            total += temp_list.count(sum)

            if pop_node.left:
                left_list = [item + pop_node.left.val for item in temp_list] + [pop_node.left.val]
                stack.append([pop_node.left, left_list])
            if pop_node.right:
                right_list = [item + pop_node.right.val for item in temp_list] + [pop_node.right.val]
                stack.append([pop_node.right, right_list])
        return total


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(-3)
a.left, a.right = b, c
d = TreeNode(3)
e = TreeNode(2)
b.left, b.right = d, e
f = TreeNode(11)
c.right = f
g = TreeNode(3)
h = TreeNode(-2)
d.left, d.right = g, h
i = TreeNode(1)
e.right = i

s = Solution()
res = s.pathSum(a, 8)
print(res)
