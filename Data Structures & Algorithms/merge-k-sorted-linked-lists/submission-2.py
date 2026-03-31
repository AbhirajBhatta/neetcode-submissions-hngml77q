# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists)>1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merged.append(self.mergeTwoLst(l1, l2))
            lists = merged
        return lists[0] if lists else None
    def mergeTwoLst(self, a, b):
        dummy = ListNode(0, None)
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        if a:
            tail.next = a
        else:
            tail.next = b
        return dummy.next