class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()
        def populate(r, c, dist):
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in visited or
                grid[r][c]==-1):
                return
            grid[r][c]=dist
            visited.add((r,c))
            q.append((r, c))
                
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visited:
                    visited.add((r,c))
                    q.append((r, c))
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                
                populate(r-1, c, dist)
                populate(r+1, c, dist)
                populate(r, c-1, dist)
                populate(r, c+1, dist)
            dist+=1
            