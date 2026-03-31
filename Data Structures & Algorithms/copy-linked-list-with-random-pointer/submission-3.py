"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        ogToCopy = {}
        cur = head
        while cur:
            copy = Node(cur.val)
            ogToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            cpy = ogToCopy[cur]
            cpy.next = ogToCopy[cur.next] if cur.next else None
            cpy.random = ogToCopy[cur.random] if cur.random else None
            cur = cur.next
        return ogToCopy[head] if head else None
        
