class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end=True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)
        
        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, root, word):
            if (r<0 or c<0 or
                r==rows or c ==cols or
                (r, c) in visited or board[r][c] not in root.children):
                return
            
            visited.add((r, c))
            root = root.children[board[r][c]]
            word += board[r][c]
            if root.end:
                res.add(word)
            dfs(r+1, c, root, word)
            dfs(r-1, c, root, word)
            dfs(r, c+1, root, word)
            dfs(r, c-1, root, word)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
