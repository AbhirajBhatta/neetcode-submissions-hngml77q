# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, m=float("-inf"), M=float("inf")):
            if not node:
                return True
            if node.val >= M or node.val <= m:
                return False
            res = dfs(node.left, m, node.val) and dfs(node.right, node.val, M)
            return res
        return dfs(root)