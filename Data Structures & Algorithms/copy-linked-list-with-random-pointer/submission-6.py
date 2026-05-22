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
        oldtonew = {None: None}
        tmp = head
        while tmp:
            newNode = Node(tmp.val)
            oldtonew[tmp] = newNode
            tmp = tmp.next
        tmp = head
        while tmp:
            oldtonew[tmp].next = oldtonew[tmp.next]
            oldtonew[tmp].random = oldtonew[tmp.random]
            tmp = tmp.next
        return oldtonew[head]