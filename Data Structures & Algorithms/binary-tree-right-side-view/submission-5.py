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
            
            for i in range(len(q)):
                node = q.popleft()
                if node and i==0:
                    res.append(node.val)
                if node and node.right:
                    q.append(node.right)
                if node and node.left:
                    q.append(node.left)
        return res
