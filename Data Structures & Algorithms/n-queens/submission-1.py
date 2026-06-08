class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        negdiag = set()
        self.res = []
        self.board = [["."]*n for _ in range(n)]
        def backtrack(r):
            if r==n:
                self.res.append(["".join(x) for x in self.board])
                return
            
            for c in range(n):
                if (c not in col and
                    r+c not in posdiag and
                    r-c not in negdiag):
                    col.add(c)
                    posdiag.add(r+c)
                    negdiag.add(r-c)
                    self.board[r][c] = "Q"

                    backtrack(r+1)

                    col.remove(c)
                    posdiag.remove(r+c)
                    negdiag.remove(r-c)
                    self.board[r][c] = "."
        backtrack(0)

        return self.res
