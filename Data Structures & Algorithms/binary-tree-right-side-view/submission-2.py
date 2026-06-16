# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []

        while q:
            added = 0
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if added==0:
                        res.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
                    added+=1
        return res
                