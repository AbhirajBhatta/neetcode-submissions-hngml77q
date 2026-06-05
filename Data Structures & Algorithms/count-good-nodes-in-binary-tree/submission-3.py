# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, PathGreatest):
            if not root:
                return
            if root.val >= PathGreatest:
                self.res+=1
            PathGreatest = max(PathGreatest, root.val)
            dfs(root.left, PathGreatest)
            dfs(root.right, PathGreatest)
        dfs(root, float("-inf"))
        return self.res
