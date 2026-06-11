class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visited = set()
        self.fresh = 0
        def rot(r, c):
            if (r<0 or c<0 or r==rows or c==cols or
                (r, c) in visited or grid[r][c]!=1):
                return
            grid[r][c]=2
            self.fresh-=1
            visited.add((r, c))
            q.append((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r, c))
                    visited.add((r, c))
                if grid[r][c]==1:
                    self.fresh+=1
        mins = 0
        while q and self.fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            mins+=1
        return mins if not self.fresh else -1