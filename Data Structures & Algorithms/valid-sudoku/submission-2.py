class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck = defaultdict(set)
        colcheck = defaultdict(set)
        boxcheck = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if (val in rowcheck[i]
                    or val in colcheck[j]
                    or val in boxcheck[(i//3, j//3)]
                    ):
                    return False
                rowcheck[i].add(val)
                colcheck[j].add(val)
                boxcheck[(i//3, j//3)].add(val)
        return True
                
