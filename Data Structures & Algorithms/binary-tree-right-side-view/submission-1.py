# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        while q:
            nodesEncountered = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if nodesEncountered==0:
                        res.append(node.val)
                        nodesEncountered+=1
                    q.append(node.right)
                    q.append(node.left)
        return res