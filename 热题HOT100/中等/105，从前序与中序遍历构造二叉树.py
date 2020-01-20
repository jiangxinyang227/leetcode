"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == len(inorder) == 0:
            return None

        mid_val = preorder[0]
        root = TreeNode(mid_val)
        index = inorder.index(mid_val)
        root.left = self.buildTree(preorder[1: index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])

        return root

    def dfs(self, root):
        if root is None:
            return

        stack = []
        cur = root
        while stack or cur:
            if cur:
                print(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()


s = Solution()
res = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
s.dfs(res)
