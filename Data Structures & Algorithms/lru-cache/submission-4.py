class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, Node):
        nxt, prev = Node.next, Node.prev
        prev.next = nxt
        nxt.prev = prev
        Node.next = Node.prev = None
    def add(self, Node):
        nxt, prev = self.right, self.right.prev
        Node.next, Node.prev = nxt, prev
        nxt.prev = prev.next = Node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
        else:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            self.cache[key].val = value

        

