# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        Curr = head
        while Curr != None:
            temp = Curr
            Curr = Curr.next
            temp.next = prev
            prev = temp
        return prev
            
            