class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        cur.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        rows, cols = len(board), len(board[0])
        visited = set()
        root = TrieNode()
        for w in words:
            root.add(w)
        
        def dfs(r, c, node, cur):
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in visited or 
                board[r][c] not in node.children
                ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            cur += board[r][c]
            if node.end:
                res.add(cur)
            dfs(r+1, c, node, cur)
            dfs(r-1, c, node, cur)
            dfs(r, c+1, node, cur)
            dfs(r, c-1, node, cur)
            visited.remove((r, c))
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)