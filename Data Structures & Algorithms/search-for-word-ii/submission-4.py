class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addWord(self, w):
        cur = self
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    def inTrie(self, w):
        cur = self
        for c in w:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        res = set()
        visited = set()
        def dfs(r, c, root, cur):
            if (r<0 or c<0 or
                r==rows or c==cols or
                board[r][c] not in root.children or
                (r, c) in visited):
                return
            visited.add((r, c))
            root = root.children[board[r][c]]
            cur += board[r][c]
            if root.end:
                res.add(cur)
            dfs(r+1, c, root, cur)
            dfs(r-1, c, root, cur)
            dfs(r, c-1, root, cur)
            dfs(r, c+1, root, cur)
            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)