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
            kth = self.getKth(grpPrev, k)
            if not kth:
                return dummy.next
            prv = kth.next
            grpNext = kth.next
            curr = grpPrev.next
            while curr!=grpNext:
                tmp = curr.next 
                curr.next = prv
                prv = curr
                curr = tmp
            tmp = grpPrev.next
            grpPrev.next = kth
            grpPrev = tmp
    def getKth(self, head, k):
        while head and k>0:
            head = head.next
            k-=1
        return head
