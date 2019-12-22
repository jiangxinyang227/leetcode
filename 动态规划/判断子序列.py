"""

"""


def is_sub_sequence(s, t):
    s_point = 0
    t_point = 0

    s_l = len(s)
    t_l = len(t)

    while s_point < s_l and t_point < t_l:
        if s[s_point] == t[t_point]:
            s_point += 1
        t_point += 1
    return s_point == s_l

a = "abc"
b = "achbgc"
result = is_sub_sequence(a, b)
print(result)
