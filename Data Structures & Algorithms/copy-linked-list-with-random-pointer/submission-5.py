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
        oldToNew = {None:None}
        tmp = head
        while tmp:
            newNode = Node(tmp.val)
            oldToNew[tmp] = newNode
            tmp = tmp.next
        old = head
        while old:
            oldToNew[old].next = oldToNew[old.next]
            oldToNew[old].random = oldToNew[old.random]
            old = old.next
        return oldToNew[head]