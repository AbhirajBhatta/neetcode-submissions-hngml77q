class ListNode:
    def __init__(self, key = -1, val=0, prev=None, next=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left

    def add(self, node):
        prv, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prv
        prv.next, nxt.prev = node, node

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next = nxt
        nxt.prev = prv
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = ListNode(key, value)
            self.add(self.cache[key])
            if len(self.cache)>self.capacity:
                tmp = self.left.next
                self.remove(tmp)
                del self.cache[tmp.key]
