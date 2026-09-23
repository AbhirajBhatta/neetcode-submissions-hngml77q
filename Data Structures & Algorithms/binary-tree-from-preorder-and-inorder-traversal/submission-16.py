# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndex = {v:i for i, v in enumerate(inorder)}
        prdx = 0
        def construct(l, r):
            nonlocal prdx
            if l>r:
                return None
            root_val = preorder[prdx]
            prdx+=1
            root = TreeNode(root_val)
            index = inorderIndex[root_val]
            root.left = construct(l, index-1)
            root.right = construct(index+1, r)
            
            return root
        return construct(0, len(inorder)-1)