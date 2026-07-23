class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        negDiag, posDiag, Col = set(), set(), set()

        res = []
        board = [["."]*n for i in range(n)]
        
        def backtrack(row):
            if row==n:
                res.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if (col in Col or row+col in posDiag or row-col in negDiag):
                    continue
                
                board[row][col] = "Q"
                negDiag.add(row-col)
                posDiag.add(row+col)
                Col.add(col)

                backtrack(row+1)
            
                board[row][col] = "."
                negDiag.remove(row-col)
                posDiag.remove(row+col)
                Col.remove(col)
        backtrack(0)
        return res
