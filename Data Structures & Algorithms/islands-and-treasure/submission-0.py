class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def visit(r, c):
            if (r<0 or c<0 or r==rows or c==cols
                or (r, c) in visited or grid[r][c]==-1):
                return
            grid[r][c]=dist
            visited.add((r,c))
            q.append((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r, c))
                    visited.add((r, c))
        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit(r-1, c)
                visit(r+1, c)
                visit(r, c-1)
                visit(r, c+1)
            dist+=1