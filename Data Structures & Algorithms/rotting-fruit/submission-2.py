class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        healthy = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    healthy+=1
                if grid[r][c]==2 and (r, c) not in visited:
                    visited.add((r, c))
                    q.append([r, c])
        def rot(r, c):
            nonlocal healthy
            if (r<0 or c<0 or r==rows or c==cols
                or (r, c) in visited or grid[r][c]!=1):
                return
            grid[r][c]=2
            healthy-=1
            visited.add((r, c))
            q.append([r, c])
        mins = 0
        while q and healthy>0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            mins+=1
        return mins if not healthy else -1