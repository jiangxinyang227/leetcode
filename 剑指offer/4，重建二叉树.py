"""
根据树的前序遍历和中序遍历构建二叉树
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, node=None):
        self.root = node

    def add(self, val):
        """
        用层序遍历实现二叉树的加法
        :param val:
        :return:
        """
        node = TreeNode(val)
        if self.root is None:
            self.root = node

        else:
            queue = []
            queue.append(self.root)

            while queue:
                pop_node = queue.pop(0)

                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    queue.append(pop_node.left)
                    queue.append(pop_node.right)

    def bfs(self, root):
        """
        层序遍历
        :param root:
        :return:
        """
        if root is None:
            return None

        queue = [root]
        while queue:
            pop_node = queue.pop(0)
            print(pop_node.val)
            if pop_node.left is not None:
                queue.append(pop_node.left)
            if pop_node.right is not None:
                queue.append(pop_node.right)

    def front_dfs_rec(self, root):
        """
        前序遍历，中左右，只要将左子树和右子树看作一个新的树递归就行了，递归的终止条件就是该节点为None
        :param root:
        :return:
        """
        if root is None:
            return []

        return [root.val] + self.front_dfs_rec(root.left) + self.front_dfs_rec(root.right)

    def mid_dfs_rec(self, root):
        """
        中序遍历，左中右
        :param root:
        :return:
        """
        if root is None:
            return []
        return self.mid_dfs_rec(root.left) + [root.val] + self.mid_dfs_rec(root.right)

    def back_dfs_rec(self, root):
        """
        后序遍历，左右中
        :param root:
        :return:
        """
        if root is None:
            return []
        return self.back_dfs_rec(root.left) + self.back_dfs_rec(root.right) + [root.val]

    def front_dfs(self, root):
        """
        使用循环的方法实现, 中左右 在这里需要用到栈来保存未遍历的右子树
        :param root:
        :return:
        """
        stack = []
        result = []
        cur = root

        while cur or stack:
            if cur:
                result.append(cur.val)  # 先将当前树的根节点取出
                stack.append(cur.right)  # 将右子树存到栈中
                cur = cur.left  # 然后再将左子树执行上述操作
            else:
                cur = stack.pop()  # 当达到了最下面的左子树时会取栈中的右子树出来，利用先进后出的思想
        return result

    def mid_dfs(self, root):
        """
        使用循环的方法实现，左中右
        :param root:
        :return:
        """
        stack = []
        result = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                pop_node = stack.pop()
                result.append(pop_node.val)
                cur = pop_node.right
        return result

    def back_dfs(self, root):
        """
        使用循环的方法实现，左右中
        :param root:
        :return:
        """
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            pop_node = stack.pop()
            if isinstance(pop_node, int):
                result.append(pop_node)
            else:
                stack.append(pop_node.val)
                if pop_node.right:
                    stack.append(pop_node.right)
                if pop_node.left:
                    stack.append(pop_node.left)
        return result


def reconstruct_tree(pre, mid):
    if len(pre) < 1 and len(mid) < 1:
        return None

    if len(pre) != len(mid):
        return None

    root = TreeNode(pre[0])
    index = mid.index(pre[0])
    root.right = reconstruct_tree(pre[index + 1:], mid[index + 1:])
    root.left = reconstruct_tree(pre[1:index + 1], mid[:index])
    return root


pre_list = [1, 2, 4, 5, 3, 6, 7]
mid_list = [4, 2, 5, 1, 6, 3, 7]
tree_root = reconstruct_tree(pre_list, mid_list)

# datas = [1, 2, 3, 4, 5, 6, 7]
tree = Tree()
# for data in datas:
#     tree.add(data)

tree.bfs(tree_root)
print("------------------")
res = tree.front_dfs_rec(tree_root)
print(tree.front_dfs(tree_root))
print(res)
print("-----------------")
print(tree.mid_dfs_rec(tree_root))
print(tree.mid_dfs(tree_root))
print("--------------------")
print(tree.back_dfs_rec(tree_root))
print(tree.back_dfs(tree_root))
print("----------")
