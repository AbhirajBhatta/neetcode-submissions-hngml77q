# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        largest = root.val
        def dfs(node, prevLargest):
            if not node:
                return
            if node.val >= prevLargest:
                prevLargest = node.val
                self.res+=1
            dfs(node.left, prevLargest)
            dfs(node.right, prevLargest)
        dfs(root, root.val)
        return self.res