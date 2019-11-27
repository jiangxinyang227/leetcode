"""
对于一个行从左到右升序，列从上到下升序的二维数组，查找一个元素
典型的方法是从四个角上找一个起始点，但这个其实点得符合往两个方向走的升降序上相反的，比如可以选择左下或右上
"""


def search_matrix(matrix, target):

    if matrix == [] or matrix == [[]]:
        return False

    row = len(matrix)
    col = len(matrix[0])

    row_index = row - 1
    col_index = 0

    while row_index >= 0 and col_index < col:
        if target == matrix[row_index][col_index]:
            return True
        elif target > matrix[row_index][col_index]:
            col_index += 1
        else:
            row_index -= 1
    return False


array = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

res = search_matrix(array, 32)
print(res)