"""
给定一个二叉树的根节点，给定一个整数值，从根节点开始，找出所有满足路径上节点和等于该整数值的路径集合

解法一：采用递归的方法求解
解法二，可以用一个栈来实现从不同的序列出发
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_path(root, expect_number):
    if root is None:
        return []
    if root.left is None and root.right is None and root.val == expect_number:
        return [[root.val]]

    left = find_path(root.left, expect_number - root.val)
    right = find_path(root.right, expect_number - root.val)

    res = []
    for item in left + right:
        res.append([root.val] + item)

    return res


def find_path_1(root, expect_number):
    if root is None:
        return []
    stack = [[root, [root.val]]]
    result = []
    while stack:
        pop_node, temp_list = stack.pop()
        if sum(temp_list) == expect_number:
            result.append(temp_list)
        if pop_node.left:
            left_list = temp_list + [pop_node.left.val]
            stack.append([pop_node.left, left_list])
        if pop_node.right:
            right_list = temp_list + [pop_node.right.val]
            stack.append([pop_node.right, right_list])
    return result


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(6)
f = TreeNode(3)

a.left = b
a.right = c
b.left = d
c.left = e
d.left = f

res = find_path(a, 10)
print(res)
res1 = find_path_1(a, 10)
print("using stack: ", res1)
