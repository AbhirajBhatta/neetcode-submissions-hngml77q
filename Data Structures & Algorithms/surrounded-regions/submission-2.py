class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        NotSurrrounded = set()
        def dfs(r, c):
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in NotSurrrounded or
                board[r][c]=="X"):
                return
            NotSurrrounded.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in NotSurrrounded and board[r][c]=="O":
                    board[r][c]="X"
