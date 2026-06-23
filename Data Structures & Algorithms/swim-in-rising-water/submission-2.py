class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        visited.add((0,0))
        time = 0

        minH = [[grid[0][0], 0, 0]]

        def explore(cost, x, y):
            if (x<0 or y<0 or
                x==rows or y==cols or
                (x, y) in visited):
                return
            visited.add((x, y))
            heapq.heappush(minH, [max(cost, grid[x][y]), x, y])

        while minH:
            cost, x, y = heapq.heappop(minH)
            if x==rows-1 and y==cols-1:
                return max(cost, time)
            time = max(time, cost)
            explore(time, x-1, y)
            explore(time, x+1, y)
            explore(time, x, y-1)
            explore(time, x, y+1)
        