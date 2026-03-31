# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        for i in range(1, len(lists)):
            tmp = self.merge2List(lists[i-1], lists[i])
            lists[i] = tmp
        return lists[-1] if lists else None

    def merge2List(self, l1, l2):
        res = dummy = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next
            dummy = dummy.next
        
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return res.next

