# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid, end = head, head
        while end and end.next:
            end = end.next.next
            mid = mid.next
        
        prev = None
        curr = mid.next
        mid.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        l1, l2 = head, prev
        while l2:
            t1, t2 = l1.next, l2.next
            l1.next = l2
            l2.next = t1
            l1, l2 = t1, t2
        