"""
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。
任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。

贪心法：先把最可能的执行了。即先将个数最多的任务排号，中间用空格隔开，然后用剩余的填充，碰到多个任务数量都一样多且都是最大
如上面的任务A和B都是3次，且是整个序列中数量最多的两种任务，此时还需要计算的结果中加上重复的数量任务的个数
最后当计算的序列长度小于任务数，则取任务数

计算公式 = （max_task - 1）* (n + 1) + same_task_num
"""


class Solution:
    def leastInterval(self, tasks, n: int) -> int:

        if len(tasks) <= 1:
            return len(tasks)

        statistic = {}
        for task in tasks:
            statistic[task] = statistic.get(task, 0) + 1

        sort_statis = sorted(statistic.items(), key=lambda x: x[1], reverse=True)

        res = (sort_statis[0][1] - 1) * (n + 1)
        count = 1
        for item in sort_statis[1:]:
            if item[1] == sort_statis[0][1]:
                count += 1
        res += count
        return res if res > len(tasks) else len(tasks)


s = Solution()
result = s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
print(result)
