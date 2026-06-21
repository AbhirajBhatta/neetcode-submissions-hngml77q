class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    visited.add((r, c))
                    q.append((r, c))
        dist = 1

        def explore(r, c):
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in visited or
                grid[r][c]==-1):
                return
            grid[r][c]=dist
            visited.add((r, c))
            q.append((r, c))
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                explore(r-1, c)
                explore(r+1, c)
                explore(r, c-1)
                explore(r, c+1)
            dist+=1
        
