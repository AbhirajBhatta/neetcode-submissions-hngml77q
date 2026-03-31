# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        tail = dummy

        start, fast = head, head.next
        while fast != None and fast.next!=None:
            start = start.next
            fast = fast.next.next
        
        prev = None
        curr = start.next 
        start.next = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # prev is the ptr to 2nd half reversed, and start is our first half ptr
        first, second = head, prev
        while second != None:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2


