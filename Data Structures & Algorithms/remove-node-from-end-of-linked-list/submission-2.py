# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        dummy = ListNode()
        dummy.next = head
        lptr, rptr = dummy, head
        while l != n and rptr:
            rptr = rptr.next
            l+=1
        
        while rptr!=None:
            rptr = rptr.next
            lptr = lptr.next
        lptr.next = lptr.next.next
        return dummy.next

        
        
