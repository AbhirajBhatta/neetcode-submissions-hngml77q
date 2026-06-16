# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        check = []
        def Inorder(root):
            if not root:
                return
            Inorder(root.left)
            check.append(root.val)
            Inorder(root.right)
        Inorder(root)
        valid = True
        for i in range(len(check)-1):
            if check[i+1]<=check[i]:
                valid=False
                break
        return valid