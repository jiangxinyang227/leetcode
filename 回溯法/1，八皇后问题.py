"""
采用回溯法，一个一个皇后的排列，如果最终的结果不符，则回溯到上一步，仍不符，则接着回溯
"""


def is_rule(queens, new_queen):
    length = len(queens)

    for index, queen in enumerate(queens):
        if new_queen == queen:  # 如果两个皇后位于同一列
            return False
        if abs(new_queen - queen) == length - index:  # 即行号的差和列号的差的绝对值相等，即两个皇后位于对角线
            return False
    return True


def arrange_queen(num, queen_tup=list()):
    """
    :param num:棋盘的的行数，当然数值也等于棋盘的列数
    :param queen_tup: 设置一个空队列，用于保存符合规则的棋子的信息
    """

    for new_queen in range(num):  # 遍历一行棋子的每一列

        if is_rule(queen_tup, new_queen):  # 判断是否冲突

            if len(queen_tup) == num - 1:  # 判断是否是最后一行
                yield [new_queen]  # yield关键字

            else:
                # 若果不是最后一行，递归函数接着放置棋子
                for result in arrange_queen(num, queen_tup + [new_queen]):
                    yield [new_queen] + result


# for i in arrange_queen(8):
#     print(i)


def queen(A, cur=0):
    if cur == len(A):
        print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur + 1)


queen([None] * 8)
