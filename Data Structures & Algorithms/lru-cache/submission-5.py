class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, node):
        prev, next = self.tail.prev, self.tail
        node.next, node.prev = next, prev
        next.prev, prev.next = node, node

    def delete(self, node):
        prev, next = node.prev, node.next
        node.next = node.prev = None
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.delete(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.delete(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
        self.add(self.cache[key])
        if len(self.cache) > self.capacity:
            oldest = self.head.next
            self.delete(oldest)
            del self.cache[oldest.key]
            
        

