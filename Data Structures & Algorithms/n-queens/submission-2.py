class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        negdiag = set()

        board = [["."]*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r==n:
                res.append(["".join(x) for x in board])
                return
            
            for c in range(n):
                if c in col or r-c in negdiag or r+c in posdiag:
                    continue

                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res
