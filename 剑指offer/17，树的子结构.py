"""
判断树B是不是树A的子结构，预先设定空树不是任何树的子结构
利用双递归来求解
一，首先取出树A中的子结构和树B比较，采用递归去获取树A的子结构
二，对比树A的子结构和树B是否相等时可以采用递归对比
因此只要构建两个递归函数即可

定义递归函数的时候要明确边界条件，而且边界条件只有在特殊情况下才会触发，因此不可以写成if else这种结构，只能if
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_subtree(root1, root2):
    if root2 is None:
        return False
    if root1 is None:
        return False
    return is_subtree(root1, root2) or has_subtree(root1.left, root2) or has_subtree(root1.right, root2)


def is_subtree(root1, root2):
    """
    判断两个树是否相同
    :param root1:
    :param root2:
    :return:
    """
    if root2 is None:
        return True
    if root1 is None:
        return False
    if root1.val != root2.val:
        return False

    return is_subtree(root1.left, root2.left) and is_subtree(root1.right, root2.right)
