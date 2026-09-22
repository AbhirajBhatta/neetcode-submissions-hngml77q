# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorderArr = []
        def inorder(root):
            if not root:
                return
            if len(inorderArr)==k:
                return
            inorder(root.left)
            inorderArr.append(root.val)
            inorder(root.right)
        inorder(root)
        return inorderArr[k-1]
        