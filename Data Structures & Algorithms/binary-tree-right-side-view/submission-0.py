# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        q.append(root)
        while q:
            l = len(q)
            currLvl = []
            for i in range(l):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    currLvl.append(node.val)
            if currLvl:
                res.append(currLvl[-1])
        return res
