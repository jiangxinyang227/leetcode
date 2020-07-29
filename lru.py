class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_end(self, key):
        node = self.hash_map[key]
        node.next.prev = node.prev
        node.prev.next = node.next

        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.move_to_end(key)
            return self.hash_map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].value = value
            self.move_to_end(key)
        else:
            if len(self.hash_map) == self.capacity:
                pop_node = self.head.next
                self.hash_map.pop(pop_node.key)
                self.head.next = pop_node.next
                pop_node.next.prev = self.head
                pop_node.prev = None
                pop_node.next = None
            new_node = ListNode(key, value)
            self.hash_map[key] = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev = new_node
            new_node.prev.next = new_node
