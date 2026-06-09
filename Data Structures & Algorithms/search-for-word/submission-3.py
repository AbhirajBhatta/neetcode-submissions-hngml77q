class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows, cols = len(board), len(board[0])
        def dfs(cur, i, j):
            if cur==len(word):
                return True
            
            if (i >= rows or i < 0 or
                j >= cols or j < 0 or
                (i, j) in visited or
                board[i][j]!= word[cur]):
                return False
            visited.add((i,j))
            res = (dfs(cur+1, i+1, j) or
                dfs(cur+1, i-1, j) or
                dfs(cur+1, i, j+1) or
                dfs(cur+1, i, j-1))
            visited.remove((i,j))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if dfs(0, i, j):
                    return True
        return False
