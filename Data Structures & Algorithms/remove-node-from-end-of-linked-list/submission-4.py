# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        new = ListNode(0, head)
        slow, fast = new, new.next
        while fast and n > 0:
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return new.next