"""
动态规划求解，可以将问题转化为子问题的优化
状态转移方程：f(n+1) = max(f(n), f(n-1) + array[n+1]) , 其中f(n)表示前n间房子的最大偷窃数
"""


def rob(array):
    pre, cur = 0, 0
    for item in array:
        cur, pre = max(cur, pre + item), cur

    return cur


nums = [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50, 81,
        185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]
res = rob(nums)
print(res)
