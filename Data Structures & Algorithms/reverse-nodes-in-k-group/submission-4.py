# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy
        while True:
            kth = self.getkth(grpPrev, k)
            if not kth:
                return dummy.next
            grpnext = kth.next
            curr = grpPrev.next
            prev = grpnext
            while curr!=grpnext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = grpPrev.next
            grpPrev.next = kth
            grpPrev = tmp
    def getkth(self, head, k):
        while head and k>0:
            head = head.next
            k-=1
        return head