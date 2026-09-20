# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            tmp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                tmp.append(self.merge2Lists(l1, l2))
            lists = tmp
        return lists[0]

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        tal = dummy

        while l1 and l2:
            if l1.val<=l2.val:
                tal.next = l1
                l1 = l1.next
            else:
                tal.next = l2
                l2 = l2.next
            tal = tal.next
        
        if l1:
            tal.next = l1
        else:
            tal.next = l2
        return dummy.next