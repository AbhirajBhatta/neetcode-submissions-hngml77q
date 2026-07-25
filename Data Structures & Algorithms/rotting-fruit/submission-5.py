class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        fresh = 0
        q = deque()
        visited = set()
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r, c))
                    visited.add((r, c))

        time = 0
        def rot(r, c):
            nonlocal fresh
            if (r<0 or c<0 or 
                r==rows or c==cols or
                (r, c) in visited or
                grid[r][c]!=1
                ):
                return
            visited.add((r, c))
            grid[r][c]=2
            fresh-=1
            q.append((r, c))

        while q and fresh:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r+1, c)
                rot(r-1, c)
                rot(r, c+1)
                rot(r, c-1)
            time+=1
        return time if not fresh else -1
        
