# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, m = float("-inf"), M= float("inf")):
            if not root:
                return True
            if m >= root.val or M <= root.val:
                return False
            return dfs(root.left, m ,root.val) and dfs(root.right, root.val, M)
        return dfs(root)