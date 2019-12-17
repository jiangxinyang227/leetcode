"""

"""


def print_matrix(matrix):

    if len(matrix) == 1:
        return matrix[0]

    if len(matrix[0]) == 1:
        return [row[0] for row in matrix]

    row_l = 0
    row_h = len(matrix)
    col_l = 0
    col_h = len(matrix[0])
    l = []
    while row_l < row_h and col_l < col_h:
        for item in matrix[row_l][col_l: col_h]:
            l.append(item)
        row_l += 1

        if row_l == row_h:
            break

        for item in [row[col_h - 1] for row in matrix[row_l: row_h]]:
            l.append(item)
        col_h -= 1

        if col_l == col_h:
            break

        for item in matrix[row_h - 1][col_l: col_h][::-1]:
            l.append(item)
        row_h -= 1

        if row_l == row_h:
            break

        for item in [row[col_l] for row in matrix[row_l: row_h]][::-1]:
            l.append(item)
        col_l += 1

    return l


m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
res = print_matrix(m)
print(res)