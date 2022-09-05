# 2022/08/17
# 超过了13.24%
# 执行用时: 792 ms
# 内存消耗: 72.1 MB
from utils import LinkedNode


class LRUCache:
    def __init__(self, capacity):
        # initialize a dict to ensure O(1) search time
        self.cache = {}
        # create fake head and tail node to deal with border
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = LinkedNode(key=key, value=value)
            self.cache[key] = node
            self.add_to_head(node)
            if len(self.cache) > self.capacity:
                node = self.remove_tail()
                # do not forget to pop
                self.cache.pop(node.key)
        else:
            node = self.cache[key]
            node.value = value
            self.cache[key] = node
            self.move_to_head(node)

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    @staticmethod
    # remember to return node
    def remove_node(node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def move_to_head(self, node):
        node = self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        node = self.remove_node(self.tail.prev)
        node.prev.next = self.tail
        self.tail.prev = node.prev
        return node


if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    print(f"Expected result: 1")
    print(f"Outcome result: {lru_cache.get(1)}")
    lru_cache.put(3, 3)
    print(f"Expected result: -1")
    print(f"Outcome result: {lru_cache.get(2)}")
    lru_cache.put(4, 4)
    lru_cache.get(1)
    print(f"Expected result: -1")
    print(f"Outcome result: {lru_cache.get(1)}")
    lru_cache.get(3)
    print(f"Expected result: 3")
    print(f"Outcome result: {lru_cache.get(3)}")
    lru_cache.get(4)
    print(f"Expected result: 4")
    print(f"Outcome result: {lru_cache.get(4)}")
