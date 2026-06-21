class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    visited.add((r, c))
                    q.append((r, c))

        def rot(r, c):
            nonlocal fresh
            if (r<0 or c<0 or
                r==rows or c==cols or
                (r, c) in visited or
                grid[r][c]!=1):
                return
            grid[r][c]=2
            fresh-=1
            visited.add((r, c))
            q.append((r, c))
        time = 0
        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r-1, c)
                rot(r+1, c)
                rot(r, c-1)
                rot(r, c+1)
            time+=1
        return time if not fresh else -1