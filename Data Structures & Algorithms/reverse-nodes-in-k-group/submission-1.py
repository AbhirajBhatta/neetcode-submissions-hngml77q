# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k) 
            if not kth:
                break
            
            groupNext = kth.next
            curr, prev = groupPrev.next, groupNext

            while curr!=groupNext:
                tmp = curr.next 
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
            
    def getKth(self, l, k):
        res = l
        while k>0 and res:
            res = res.next
            k-=1
        return res
            
