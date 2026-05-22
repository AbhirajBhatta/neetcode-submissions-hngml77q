# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        h1, h2 = head, prev

        while h2:
            t1, t2 = h1.next, h2.next
            h1.next, h2.next = h2, t1
            h1, h2 = t1, t2
