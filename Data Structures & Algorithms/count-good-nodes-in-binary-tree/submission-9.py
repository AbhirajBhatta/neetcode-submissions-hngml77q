# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(maxNode, root):
            if not root:
                return
            
            if root.val >= maxNode:
                self.res+=1
                maxNode = root.val
            
            dfs(maxNode, root.left)
            dfs(maxNode, root.right)
        dfs(-101, root)
        return self.res
