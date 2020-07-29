class PriorQueue:
    def __init__(self, elements=()):
        self.elements = list(elements)
        if self.elements:
            self.build_heap()

    def is_empty(self):
        return not self.elements

    def enqueue(self, val):
        self.elements.append(val)
        self.sift_up(val, len(self.elements) - 1)

    def dequeue(self):
        ret_val = self.elements[0]
        pop_val = self.elements.pop()
        self.sift_down(pop_val, 0, len(self.elements))
        return ret_val

    def sift_up(self, val, end):
        son, father = end, (end - 1) // 2
        while son > 0 and self.elements[father] > val:
            self.elements[son] = self.elements[father]
            son, father = father, (father - 1) // 2
        self.elements[son] = val

    def sift_down(self, val, begin, end):
        father, left_son = begin, 2 * begin + 1
        while left_son < end:
            if left_son + 1 < end and self.elements[left_son] > self.elements[left_son + 1]:
                left_son += 1
            if val < self.elements[left_son]:
                break
            self.elements[father] = self.elements[left_son]
            father, left_son = left_son, left_son * 2 + 1
        self.elements[father] = val

    def build_heap(self):
        end = len(self.elements)
        for i in range((end // 2) - 1, -1, -1):
            self.sift_down(self.elements[i], i, end)


if __name__ == "__main__":
    temp = PriorQueue([5, 6, 8, 1, 2, 4, 9])
    print(temp.elements)
    temp.dequeue()
    print(temp.elements)
    temp.enqueue(0)
    print(temp.elements)
