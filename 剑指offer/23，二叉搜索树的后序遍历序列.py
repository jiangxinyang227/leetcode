"""
利用二叉搜索树的性质，如果二叉搜索树的左子树存在，则左子树上所有的节点值小于根节点，
如果二叉搜索树的右子树存在，则右子树所有节点值大于根节点
且左子树和右子树也为二叉搜索树
解题思路：可以用递归来实现
"""


def verify_sequence_of_bst(array):
    if len(array) == 0:
        return False
    if len(array) == 1:
        return True

    root = array[-1]
    split_index = 0
    for i in range(len(array)):
        if array[i] < root:
            split_index = i
        else:
            break

    for item in array[split_index + 1:]:
        if item < root:
            return False

    left = True
    right = True
    if len(array[:split_index + 1]) > 0:
        left = verify_sequence_of_bst(array[:split_index + 1])
    if len(array[split_index + 1: -1]) > 0:
        right = verify_sequence_of_bst(array[split_index + 1: -1])
    return left and right


a = [7, 8, 6, 12, 14, 10]
res = verify_sequence_of_bst(a)
print(res)
