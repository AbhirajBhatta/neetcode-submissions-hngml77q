class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        minH = [[grid[0][0], 0, 0]]

        def explore(r, c, cost):
            if (r<0 or c<0 or
                r==n or c==n or
                (r, c) in visited):
                return
            visited.add((r, c))
            heapq.heappush(minH, [max(cost, grid[r][c]), r, c])
        while minH:
            cost, r, c = heapq.heappop(minH)
            if r==n-1 and c==n-1:
                return cost
            explore(r-1, c, cost)
            explore(r+1, c, cost)
            explore(r, c-1, cost)
            explore(r, c+1, cost)
            

