class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def bfs(r, c):
            q.append((r, c))
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if (r<0 or c<0 or
                        r==rows or c==cols or
                        (r, c) in visited or
                        grid[r][c]=="0"):
                        continue
                    visited.add((r, c))
                    q.append((r-1, c))
                    q.append((r+1, c))
                    q.append((r, c-1))
                    q.append((r, c+1))
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c]=="1":
                    bfs(r, c)
                    res+=1
        return res
