"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""


class Solution:
    def has_path(self, matrix, rows, cols, path):
        for ri in range(rows):
            for ci in range(cols):
                mask = [0] * (rows * cols)
                if self.find(list(matrix), rows, cols, path, ri, ci, mask, 0):
                    return True
        return False

    def find(self, matrix, rows, cols, path, ri, ci, mask, index):
        if not (0 <= ci < cols - 1 and 0 <= ri < rows - 1):
            return False
        if mask[ri * cols + ci] != 0:
            return False
        if index == len(path):
            return True
        if matrix[ri * cols + ci] == path[index]:
            mask[ri * cols + ci] = 1
        if self.find(matrix, rows, cols, path, ri, ci + 1, mask, index + 1) or self.find(matrix, rows, cols, path, ri, ci - 1, mask, index + 1) or self.find(matrix, rows, cols, path, ri + 1, ci, mask, index + 1) or self.find(matrix, rows, cols, path, ri - 1, ci, mask, index + 1):
            return True
        else:
            return False


st = Solution()
matrix = 'abtgcfcsjdeh'
path = 'bfce'
print(st.has_path(matrix, 3, 4, path))
