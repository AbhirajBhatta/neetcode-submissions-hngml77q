class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r, c))
                    visited.add((r, c))

        def explore(r, c):
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in visited or
                grid[r][c]==-1):
                return
            visited.add((r, c))
            grid[r][c]=dist
            q.append((r, c))


        dist = 1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                explore(row+1, col)
                explore(row-1, col)
                explore(row, col-1)
                explore(row, col+1)
            dist+=1
        
