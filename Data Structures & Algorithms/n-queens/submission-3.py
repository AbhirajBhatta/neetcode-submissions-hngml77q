class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."]*n for _ in range(n)]
        posDiag = set()
        negDiag = set()
        cols = set()
        res = []
        def findQueens(row):
            if row==n:
                res.append(["".join(x) for x in grid])
                return
            for col in range(n):
                if ((row-col) in negDiag or
                    (row+col) in posDiag or
                    col  in cols):
                    continue
                posDiag.add(row+col)
                negDiag.add(row-col)
                cols.add(col)
                grid[row][col]="Q"

                findQueens(row+1)

                posDiag.remove(row+col)
                negDiag.remove(row-col)
                cols.remove(col)
                grid[row][col]="."
        findQueens(0)
        return res

