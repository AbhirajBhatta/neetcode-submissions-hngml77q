# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l=dummy
        r=dummy
        lprev = dummy

        while left>0:
            l = l.next
            left-=1
        while right>0:
            r = r.next
            right-=1
        while lprev.next != l:
            lprev = lprev.next
        prev = r.next
        end = r.next
        cur = l
        while cur!=end:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        lprev.next = prev
        return dummy.next

