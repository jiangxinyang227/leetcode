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
                if matrix[ri*cols+ci] == path[0]:
                    if self.find(list(matrix), rows, cols, path[1:], ri, ci):
                        return True
        return False

    def find(self, matrix, rows, cols, path, ri, ci):
        if not path:
            return True
        matrix[ri*cols+ci] = '0'
        if ci < cols-1 and matrix[ri*cols+(ci+1)] == path[0]:
            return self.find(matrix, rows, cols, path[1:], ri, ci+1)
        elif ci > 0 and matrix[ri * cols + (ci - 1)] == path[0]:
            return self.find(matrix, rows, cols, path[1:], ri, ci-1)
        elif ri < rows - 1 and matrix[(ri + 1) * cols + ci] == path[0]:
            return self.find(matrix, rows, cols, path[1:], ri+1, ci)
        elif ri > 0 and matrix[(ri-1)*cols+ci] == path[0]:
            return self.find(matrix, rows, cols, path[1:], ri-1, ci)
        else:
            return False


st = Solution()
matrix = 'abtgcfcsjdeh'
path = 'bfce'
print(st.has_path(matrix, 3, 4, path))
