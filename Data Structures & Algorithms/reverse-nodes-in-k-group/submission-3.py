# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while True:
            kth = self.getkth(curr, k)
            if not kth: return dummy.next
            grpNext = kth.next
            prev = grpNext
            cur = curr.next
            while cur!=grpNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp = curr.next
            curr.next = kth
            curr = tmp




    def getkth(self, head, k):
        while head and k>0:
            head = head.next
            k-=1
        return head