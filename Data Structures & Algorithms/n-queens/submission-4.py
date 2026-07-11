class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posdiag = set()
        negdiag = set()
        col = set()

        board = [["."]*n for _ in range(n)]
        self.res = []
        def backtrack(r):
            if r==n:
                sol = []
                for row in board:
                    sol.append("".join(row))
                self.res.append(sol)
                return
            
            for c in range(n):
                if not (r-c in negdiag or r+c in posdiag or c in col):
                    board[r][c]="Q"
                    posdiag.add(r+c)
                    negdiag.add(r-c)
                    col.add(c)

                    backtrack(r+1)

                    board[r][c]="."
                    posdiag.remove(r+c)
                    negdiag.remove(r-c)
                    col.remove(c)
        backtrack(0)
        return self.res

            

