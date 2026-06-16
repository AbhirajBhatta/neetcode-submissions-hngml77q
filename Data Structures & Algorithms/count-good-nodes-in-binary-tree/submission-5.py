# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, maxNode):
            if not node:
                return 
            if node.val >= maxNode:
                self.res+=1
            maxNode = max(node.val, maxNode)
            dfs(node.left, maxNode)
            dfs(node.right, maxNode)
        dfs(root, float("-inf"))
        return self.res