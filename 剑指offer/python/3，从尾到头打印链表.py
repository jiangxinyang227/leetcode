"""
从尾到头遍历一遍列表
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list_from_tail_to_head(head):
    if head is None:
        return []

    cur = head
    temp = []
    while cur is not None:
        temp.append(cur.val)
        cur = cur.next
    rev_temp = temp[::-1]
    return rev_temp


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d


res = print_list_from_tail_to_head(a)
print(res)