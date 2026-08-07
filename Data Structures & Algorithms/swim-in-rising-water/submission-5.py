class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        minH = [(grid[0][0], 0, 0)]
        Highest = 0
        def explore(r, c, curCost):
            nonlocal Highest
            if (r<0 or c<0 
                or r==n or c==n or
                (r, c) in visited 
                ):
                return
            
            visited.add((r, c))
            heapq.heappush(minH, (max(curCost, grid[r][c]), r, c))
        while minH:
            for i in range(len(minH)):
                cost, i, j = heapq.heappop(minH)
                Highest = max(grid[i][j], Highest)
                if i==n-1 and j==n-1:
                    return Highest
                explore(i+1, j, cost)
                explore(i-1, j, cost)
                explore(i, j-1, cost)
                explore(i, j+1, cost)

