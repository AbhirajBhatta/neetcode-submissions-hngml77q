# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def dfs(root):
            if not root:
                self.res.append("N")
                return
            self.res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(",")
        self.i = 0

        def dfs():
            if arr[self.i]=="N": 
                self.i+=1
                return
            node = TreeNode(int(arr[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root