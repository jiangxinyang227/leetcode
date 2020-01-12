"""
给定背包容量c，物品重量列表w，物品价格列表v
采用动态规划
动态规划+优化空间
两种方式解决
"""


def zero_one_pack(dp, w_i, v_i):
    """
    更新单个背包
    :param dp:
    :param w_i:
    :param v_i:
    :return:
    """
    for i in range(len(dp), w_i - 1, -1):
        dp[i] = max(dp[i], dp[i - w_i] + v_i)


def bag(c, w, v):
    n = len(w)
    dp = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i - 1]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
    return dp[-1][-1]


def super_bag(c, w, v):
    n = len(w)
    dp = [0 for i in range(c + 1)]
    for i in range(n):
        for j in range(c, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
        print(dp)
    return dp[-1]


c = 10
w = [2, 2, 3, 1, 5, 2]
v = [2, 3, 1, 5, 4, 3]

res1 = bag(c, w, v)
res2 = super_bag(c, w, v)
print(res1)
print(res2)
