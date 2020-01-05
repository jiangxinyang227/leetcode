"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mid_order(self, root):
        if root is None:
            return None
        stack = []
        cur = root
        node_val = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                pop = stack.pop()
                node_val.append(pop.val)
                cur = pop.right
        return node_val

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        node_val = self.mid_order(root)

        left, right = 0, len(node_val) - 1
        while True:
            mid = (left + right) // 2
            if mid - left == k - 1:
                return node_val[mid]
            elif mid - left > k - 1:
                right = mid
            else:
                left = mid + 1


a = TreeNode(3)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(2)
a.left, a.right = b, c
b.right = d

s = Solution()
res = s.kthSmallest(a, 1)
print(res)
