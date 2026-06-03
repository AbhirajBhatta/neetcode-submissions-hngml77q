# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(root):
            if not root:
                return 0
            
            lmax, rmax = dfs(root.left), dfs(root.right)
            lmax, rmax = max(lmax, 0), max(rmax, 0)

            self.res = max(self.res, root.val+lmax+rmax)

            return root.val + max(lmax, rmax)
        dfs(root)
        return self.res

            
            