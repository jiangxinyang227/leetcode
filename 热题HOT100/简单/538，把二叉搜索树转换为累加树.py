"""
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

中序遍历是左中右，也可以右中左遍历，则先遍历最大的值，然后将前面所有节点的值加到当前节点上
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        if root is None:
            return None

        accumulate_sum = 0

        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                pop_node = stack.pop()
                pop_node.val += accumulate_sum
                accumulate_sum = pop_node.val
                cur = pop_node.left
        return root

    def bfs(self, root):
        if root is None:
            return None
        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            print(pop_node.val)
            if pop_node.left:
                queue.append(pop_node.left)
            if pop_node.right:
                queue.append(pop_node.right)


a = TreeNode(5)
b = TreeNode(2)
c = TreeNode(13)
a.left, a.right = b, c

s = Solution()
res = s.convertBST(a)
s.bfs(res)
