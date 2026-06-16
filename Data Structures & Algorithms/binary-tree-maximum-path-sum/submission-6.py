# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = root.val
        def dfs(root):
            if not root:
                return 0

            l, r = dfs(root.left), dfs(root.right)
            l = max(l, 0)
            r = max(r, 0)
            self.maxsum = max(self.maxsum, root.val + l + r)

            return root.val + max(l, r)
        dfs(root)
        return self.maxsum



            